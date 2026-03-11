#! /usr/bin/env python3
#
def neural_network_test ( ):

#*****************************************************************************80
#
## neural_network_test() tests neural_network().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 July 2022
#
#  Author:
#
#    Original Python version by Catherine Higham, Desmond Higham.
#    This version by John Burkardt.
#
#  Reference:
#
#    Catherine Higham, Desmond Higham,
#    Deep Learning: An introduction for applied mathematicians,
#    SIAM Review,
#    Volume 61, Number 4, pages 860-891,
#    November 2019.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'neural_network_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Demonstrate back propagation.' )
#
#  eta is the learning rate.
#
  eta = 0.05
  print ( '  Using learning rate eta =', eta )
#
#  it_num is the number of stochastic gradient iterations.
#
  it_num = 1000000
  print ( '  Number of iterations = ', it_num )
#
#  Run the neural network.
#
  cost = neural_network ( eta, it_num )
#
#  Plot the cost over the iteration.
#
  cost_plot ( cost )
#
#  Report change in cost.
#
  print ( '  Initial cost = ', cost[0] )
  print ( '  Final cost   = ', cost[-1] )
#
#  Terminate.
#
  print ( '' )
  print ( 'neural_network_test():' )
  print ( '  Normal end of execution.' )

  return

def neural_network ( eta, it_num ):

#*****************************************************************************80
#
## neural_network() uses back propagation to train a network.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 July 2022
#
#  Author:
#
#    Catherine Higham, Desmond Higham.
#    Modifications by John Burkardt.
#
#  Reference:
#
#    Catherine Higham, Desmond Higham,
#    Deep Learning: An introduction for applied mathematicians,
#    SIAM Review,
#    Volume 61, Number 4, pages 860-891,
#    November 2019.
#
#  Input:
#
#    real eta: the learning rate.
#
#    integer it_num: the number of stochastic gradient iterations.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng()
#
#  Data:
#
  x1 = np.array ( [ 0.1, 0.3, 0.1, 0.6, 0.4, 0.6, 0.5, 0.9, 0.4, 0.7 ] )
  x2 = np.array ( [ 0.1, 0.4, 0.5, 0.9, 0.2, 0.3, 0.6, 0.2, 0.4, 0.6 ] )

  y =  np.array( [ [ 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0 ], \
                   [ 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0 ] ] )
#
#  Initialize weights and biases.
#
  W2 = 0.5 * rng.standard_normal ( size = [ 2, 2 ] )
  W3 = 0.5 * rng.standard_normal ( size = [ 3, 2 ] )
  W4 = 0.5 * rng.standard_normal ( size = [ 2, 3 ] )

  b2 = 0.5 * rng.standard_normal ( size = [ 2, 1 ] )
  b3 = 0.5 * rng.standard_normal ( size = [ 3, 1 ] )
  b4 = 0.5 * rng.standard_normal ( size = [ 2, 1 ] )
#
#  Forward and back propagate.
#
  cost_vec = np.zeros ( it_num + 1 )

  for it in range ( 0, it_num + 1 ):

    if ( 0 < it ):
#
#  Choose a training point at random.
#
      k = rng.integers ( low = 0, high = 10, endpoint = False )
#
#  We have to force xvec and yvec to be column vectors.
#
      xvec = np.array ( [ [ x1[k]  ], [ x2[k]  ] ] )
      yvec = np.array ( [ [ y[0,k] ], [ y[1,k] ] ] )
#
#  Forward pass.
#
      a2 = activate ( xvec, W2, b2 )
      a3 = activate ( a2,   W3, b3 )
      a4 = activate ( a3,   W4, b4 )
#
#  Backward pass.
#
      delta4 = a4 * ( 1.0 - a4 ) * ( a4 - yvec )
      delta3 = a3 * ( 1.0 - a3 ) * np.dot ( W4.T, delta4 )
      delta2 = a2 * ( 1.0 - a2 ) * np.dot ( W3.T, delta3 )
#
#  Gradient step.  
#  Adjust weights and biases with a rank one update.
#
      W2 = W2 - eta * np.dot ( delta2, xvec.T )
      W3 = W3 - eta * np.dot ( delta3, a2.T )
      W4 = W4 - eta * np.dot ( delta4, a3.T )

      b2 = b2 - eta * delta2
      b3 = b3 - eta * delta3
      b4 = b4 - eta * delta4
#
#  Monitor the progress.
#
    cost_vec[it] = cost_function ( W2, W3, W4, b2, b3, b4, x1, x2, y )

  return cost_vec

def activate ( x, W, b ):

#*****************************************************************************80
#
## activate() evaluates the sigmoid function.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 May 2022
#
#  Author:
#
#    Catherine Higham, Desmond Higham
#    Modifications by John Burkardt.
#
#  Reference:
#
#    Catherine Higham, Desmond Higham,
#    Deep Learning: An introduction for applied mathematicians,
#    SIAM Review,
#    Volume 61, Number 4, pages 860-891,
#    November 2019.
#
#  Input:
#
#    x(4): the input vector.
#
#    W(4): the weights.
#
#    b(4): the shifts.
#
#  Output:
#
#    y(4): the output vector.
#
  import numpy as np

  y = 1.0 / ( 1.0 + np.exp ( - ( np.dot ( W, x ) + b ) ) )

  return y

def cost_function ( W2, W3, W4, b2, b3, b4, x1, x2, y ):

#*****************************************************************************80
#
## cost_function() evaluates the cost function.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 May 2022
#
#  Author:
#
#    Catherine Higham, Desmond Higham.
#    Modifications by John Burkardt.
#
#  Input:
#
#    real W2(), W3(), W4(): the weights.
#
#    real b2(), b3(), b4(): the shifts.
#
#    real x1(), x2():
#
#    real y():
#
#  Output:
#
#    real costval: the current value of the cost function.
#
  import numpy as np

  costvec = np.zeros ( 10 )

  for i in range ( 0, 10 ):

    x = np.zeros ( [ 2, 1 ] )
    x[0,0] = x1[i]
    x[1,0] = x2[i]
    a2 = activate ( x, W2, b2 )
    a3 = activate ( a2, W3, b3 )
    a4 = activate ( a3, W4, b4 )
    costvec[i] = np.linalg.norm ( np.transpose ( a4 ) - y[:,i]  )

  costval = np.sum ( costvec**2 )

  return costval

def cost_plot ( cost_vec ):

#*****************************************************************************80
#
## cost_plot() plots the cost function over the iterations.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 July 2022
#
#  Author:
#
#    Catherine Higham, Desmond Higham.
#    Modifications by John Burkardt.
#
#  Input:
#
#    real cost_vec(it_num+1): the cost at each iteration.
#
  import matplotlib.pyplot as plt
  import numpy as np

  it_num = cost_vec.shape[0] - 1
#
#  Plot the decay of the cost function.
#
  plt.clf ( )
  i = np.arange ( 0, it_num+1, 10000 )
  plt.semilogy ( i, cost_vec[i], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- Iteration -->' )
  plt.ylabel ( '<-- Cost -->' )
  plt.title ( 'Cost reduction during stochastic gradient descent' )
  filename = 'neural_network.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def intspace ( a, b, n ):

#*****************************************************************************80
#
## intspace() returns roughly equally spaced integers in an interval.
#
#  Discussion:
#
#    intspace() is a sort of "linspace()" for integers.
#
#    An interval is defined by integers A <= B.
#
#    If possible, a vector C of N integers is to be determined, with
#    C(1) = A and C(N) = B.
#
#    So far as possible, the entries of C should be equally spaced in [A,B].
#
#    However, if B-A+1 < N, then we simply return C = A:B.
#
#    A use for this code can be imagined in which a large array of data
#    has been computed, and it is desired to make a plot.  However, displaying
#    all the data might result in an ugly plot, or one that takes too long
#    to display.  One can then specify an index set like 
#      c = intspace ( 1, max, 100 )
#    and restrict the plot to the data indexed by C.
#
#    Similarly, it might be desired to print out sample values of a large
#    array of data; this function would make it easy to do this in a
#    fairly regular fashion.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 July 2022
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer A, B: the left and right endpoints.
#
#    integer N: the number of samples desired.
#
#  Output:
#
#    integer C[*]: the sample values.  The first and last entries
#    of C will be A and B respectively.  The number of entries in C
#    will be min ( N, B+1-A).  The entries of C will be roughly
#    equally spaced.
#
  import numpy as np

  if ( b + 1 - a <= n ):
    c = np.arange ( a, b + 1 )
  else:
    i = np.arange ( n - 1, -1, -1 )
    j = np.arange ( 0, n )
    c = np.round ( ( i * a + j * b ) / ( n - 1 ) )

  c = c.astype ( int )

  return c

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  neural_network_test ( )
  timestamp ( ) 

