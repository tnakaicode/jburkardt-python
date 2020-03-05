#! /usr/bin/env python3
#


def cvxopt_svm_test():

    # *****************************************************************************80
    #
    # cvxopt_svm determines the parameters of a support vector machine.
    #
    #  Discussion:
    #
    #    We are given m data pairs ( x_i, y_i ), with each y_i being -1 or +1.
    #
    #    The SVM problem can be described as solving:
    #      minimize    w'w
    #      subject to yi ( x'wi+b) >= 1 for 1 <= i <= m
    #
    #    The cvxopt package includes a quadratic programming option to find x:
    #      minimize   1/2 x' P x + q' x
    #      subject to G x <= h
    #                 A x = b
    #
    #    We read our problem data and arrange them in a format that allows
    #    us to call the cvxopt solver solvers.qp().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 April 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import matplotlib.pyplot as plt
    import numpy as np
    import platform

    print('')
    print('cvxopt_svm')
    print('  Python version: %s' % (platform.python_version()))
    print('  Support Vector Machine.')
#
#  Read the data.
#
    data = np.loadtxt('jet_engine.txt')

    rpm = data[:, 1]
    vib = data[:, 2]
    grade = data[:, 3]

    n = len(rpm)

    rpm_min = np.min(rpm)
    rpm_max = np.max(rpm)
    vib_min = np.min(vib)
    vib_max = np.max(vib)

    good = np.argwhere(grade == +1.0)
    bad = np.argwhere(grade == -1.0)
    n_good = len(good)
    n_bad = len(bad)
    bad_rpm_mean = np.mean(rpm[bad])
    bad_vib_mean = np.mean(vib[bad])
    good_rpm_mean = np.mean(rpm[good])
    good_vib_mean = np.mean(vib[good])

    print('')
    print('  Jet Engine Ratings:')
    print('')
    print('  Number of engines = %d' % (n))
    print('  %d good engines, and %d bad engines' % (n_good, n_bad))
    print('  %g <= RPM <= %g' % (rpm_min, rpm_max))
    print('  %g <= VIB <= %g' % (vib_min, vib_max))
    print('  GOOD: mean RPM = %g, mean VIB = %g' %
          (good_rpm_mean, good_vib_mean))
    print('  BAD:  mean RPM = %g, mean VIB = %g' %
          (bad_rpm_mean, bad_vib_mean))
    print('  %g <= VIB <= %g' % (vib_min, vib_max))
#
#  Call cvxopt to solve the quadratic programming problem.
#
    alphas = fit(rpm, vib, grade)
#
#  Report the SVM coefficients.
#
    w = alphas[0:2]
    b = alphas[2]

    print('')
    print('  SVM classifier')
    print('  f(x) = %g x0 + %g x1 + %g' % (w[0], w[1], b))
#
#  Plot the data and the SVM separating line.
#
    fig, ax = plt.subplots()

    slope = - w[0] / w[1]
    intercept = -b / w[1]
    x = np.arange(rpm_min, rpm_max)

    ax.plot(x, x * slope + intercept - 1 / w[1], 'r-')
    ax.plot(x, x * slope + intercept, 'k-')
    ax.plot(x, x * slope + intercept + 1 / w[1], 'b-')

    ax.scatter(rpm[bad], vib[bad], c='red', marker='o')
    ax.scatter(rpm[good], vib[good], c='blue', marker='+')

    plt.xlabel('<-- RPM -->')
    plt.ylabel('<-- VIB -->')
    plt.title('SVM for jet engine ratings')
    plt.grid(True)
    filename = 'cvxopt_svm.png'
    plt.savefig(filename)
    print('')
    print('  Graphics saved as "%s"' % (filename))
# plt.show ( )
    plt.clf()
#
#  Terminate.
#
    print('')
    print('cvxopt_svm')
    print('  Normal end of execution.')

    return


def fit(rpm, vib, grade):

    # *****************************************************************************80
    #
    # fit sets up and solves the quadratic programming problem.
    #
    #  Discussion:
    #
    #    We are given m data pairs ( x_i, y_i ), with each y_i being -1 or +1.
    #
    #    The SVM problem can be described as solving:
    #      minimize    w'w
    #      subject to yi ( x'wi+b) >= 1 for 1 <= i <= m
    #
    #    The cvxopt package includes a quadratic programming option to find x:
    #      minimize   1/2 x' P x + q' x
    #      subject to G x <= h
    #                 A x = b
    #
    #    We read our problem data and arrange them in a format that allows
    #    us to call the cvxopt solver solvers.qp().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 April 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real rpm(n), vib(n), grade(n), the data x, and the "rating" y.
    #
    #    Output, real alpha(3), the values of w and b.
    #
    from cvxopt import matrix
    from cvxopt import solvers
    import numpy as np

    n = len(rpm)
#
#  Set the arrays that describe our quadratic programming problem.
#
    H = 0.5 * np.array([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0]])

    f = np.zeros(3)

    A = np.array([rpm, vib, np.ones(n)])
    A = A.transpose()
    A = - np.dot(np.diag(grade), A)

    c = -1.0 * np.ones(n)
#
#  Convert arrays to CVXOPT "matrix" class.
#
    H = matrix(H)
    f = matrix(f)
    A = matrix(A)
    c = matrix(c)
#
#  Solve the quadratic programming problem.
#
    solvers.options['show_progress'] = False

    sol = solvers.qp(H, f, A, c)
#
#  Convert solution to numpy vector.
#
    alphas = np.array(sol['x'])

    return alphas


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


if __name__ == '__main__':
    timestamp()
    cvxopt_svm_test()
    timestamp()
