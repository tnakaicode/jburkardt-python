#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import torch
import platform
import time
import sys
import os
import math
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp


def pytorch_test():

    # *****************************************************************************80
    #
    # pytorch_test tests pytorch.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 January 2020
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('pytorch_test:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test pytorch.')
    print('')

    pytorch_test01()
    pytorch_test02()

    print('')
    print('pytorch_test:')
    print('  Normal end of execution.')


def pytorch_test01():

    # *****************************************************************************80
    #
    # pytorch_test01 tests pytorch.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 January 2020
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('pytorch_test01')
#
# N is batch size; D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
#
    N = 64
    D_in = 1000
    H = 100
    D_out = 10
#
# Create random input and output data
#
    print('  Create random input.')

    x = np.random.randn(N, D_in)

    print('  Create random output.')

    y = np.random.randn(N, D_out)
#
# Randomly initialize weights
#
    print('  Create random input weights.')
    w1 = np.random.randn(D_in, H)
    print('  Create random output weights.')
    w2 = np.random.randn(H, D_out)

    learning_rate = 1e-6
    for t in range(500):
        # Forward pass: compute predicted y
        h = x.dot(w1)
        h_relu = np.maximum(h, 0)
        y_pred = h_relu.dot(w2)

# Compute and print loss
        loss = np.square(y_pred - y).sum()
        print(t, loss)

# Backprop to compute gradients of w1 and w2 with respect to loss
        grad_y_pred = 2.0 * (y_pred - y)
        grad_w2 = h_relu.T.dot(grad_y_pred)
        grad_h_relu = grad_y_pred.dot(w2.T)
        grad_h = grad_h_relu.copy()
        grad_h[h < 0] = 0
        grad_w1 = x.T.dot(grad_h)

# Update weights
        w1 -= learning_rate * grad_w1
        w2 -= learning_rate * grad_w2

    print('')
    print('pytorch_test01:')
    print('  Normal end of execution.')

    return


def pytorch_test02():

    # *****************************************************************************80
    #
    # pytorch_test02 tests pytorch.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 January 2020
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('pytorch_test02')

    dtype = torch.float
    device = torch.device("cpu")
# device = torch.device("cuda:0") # Uncomment this to run on GPU

# N is batch size; D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
    N, D_in, H, D_out = 64, 1000, 100, 10

# Create random input and output data
    x = torch.randn(N, D_in, device=device, dtype=dtype)
    y = torch.randn(N, D_out, device=device, dtype=dtype)

# Randomly initialize weights
    w1 = torch.randn(D_in, H, device=device, dtype=dtype)
    w2 = torch.randn(H, D_out, device=device, dtype=dtype)

    learning_rate = 1e-6
    for t in range(500):
        # Forward pass: compute predicted y
        h = x.mm(w1)
        h_relu = h.clamp(min=0)
        y_pred = h_relu.mm(w2)

# Compute and print loss
        loss = (y_pred - y).pow(2).sum().item()
        print(t, loss)

# Backprop to compute gradients of w1 and w2 with respect to loss
        grad_y_pred = 2.0 * (y_pred - y)
        grad_w2 = h_relu.t().mm(grad_y_pred)
        grad_h_relu = grad_y_pred.mm(w2.t())
        grad_h = grad_h_relu.clone()
        grad_h[h < 0] = 0
        grad_w1 = x.t().mm(grad_h)

# Update weights using gradient descent
        w1 -= learning_rate * grad_w1
        w2 -= learning_rate * grad_w2

    print('')
    print('pytorch_test02:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    pytorch_test()
    timestamp()
