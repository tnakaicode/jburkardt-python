#! /usr/bin/env python3
#
def convergence_test ( ):

#*****************************************************************************80
#
## convergence_test() tests convergence().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'convergence_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test convergence().' )

  convergence_n_test01 ( )
  convergence_n_test02 ( )

  convergence_h_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'convergence_test():' )
  print ( '  Normal end of execution.' )

  return

def convergence_h ( h, e ):

#*****************************************************************************80
#
## convergence_h() estimates the h-based order of convergence.
#
#  Discussion:
#
#    We assume that the exact solution of a problem is known, and that 
#    nn successive approximations to this solution have been made.
#    The mesh size for the k-th approximation is h(k).
#    The absolute error in the k-th approximation is given as e(k).
#    This code estimates the order of convergence using successive
#    pairs of errors:
#      eoc(k) = log ( e(k-1) / e(k) ) / log ( h(k-1) / h(k) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real h(nn): the mesh size associated with each approximation.
#    Typically, the next value is half the previous one.
#
#    real e(nn): the error for each value of h.  These must be strictly
#    positive, nonzero values.
#
#  Output:
#
#    real eoc(nn): the estimates for convergence order.  eoc(1) is not
#    defined, and is returned as NaN.
#
  import numpy as np

  nn = e.size

  eoc = np.zeros ( nn )

  for k in range ( 0, nn ):
    if ( k == 0 ):
      eoc[k] = np.NaN
    else:
      eoc[k] = np.log ( e[k-1] / e[k] ) / np.log ( h[k-1] / h[k] )

  return eoc

def convergence_h_test01 ( ):

#*****************************************************************************80
#
## convergence_h_test01() tests convergence_h() on a set of ? results.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'convergence_h_test01():' )
  print ( '  A computation has been carried out with intervals,' )
  print ( '  of size h(k), for k = 1 to 5.  For each h, the' )
  print ( '  approximation error e(k) was computed.' )
  print ( '  convergence_h() estimates the convergence order.' )

  nn = 5
  h = np.array ( [ 0.25,     0.125,     0.0625,     0.03125,    0.015625 ] )
  e = np.array ( [ 0.069288, 0.0185749, 0.00479553, 0.00121795, 0.000306885 ] )

  print ( '' )
  print ( '  The number of computations was ', nn )
  print ( '  The mesh sizes h(k):' )
  print ( h )
  print ( '  The errors e(k):' )
  print ( e )
#
#  Request convergence order estimates.
#
  eoc = convergence_h ( h, e )

  eoc_mean = np.mean ( eoc[1:] )

  print ( '' )
  print ( '    h(k)  error(k)   eoc(k)' )
  print ( '' )
  for k in range ( 0, nn ):
    print ( '  %.6f  %.2e  %.2f' % ( h[k], e[k], eoc[k] ) )

  print ( '' )
  print ( '  eoc mean            %.2f' % ( eoc_mean ) )

  return

def convergence_n ( n, e ):

#*****************************************************************************80
#
## convergence() estimates the n-based order of convergence.
#
#  Discussion:
#
#    We assume that the exact solution of a problem is known, and that 
#    nn successive approximations to this solution have been made.
#    The order (number of intervals or nodes) used in the k-th approximation 
#    is n(k).
#    The absolute error in the k-th approximation is given as e(k).
#    This code estimates the order of convergence using successive
#    pairs of errors:
#      eoc(k) = log ( e(k-1) / e(k) ) / log ( n(k) / n(k-1) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real n(nn): the number of nodes or intervals used at each step.
#    Typically, the next value is twice the previous one.
#
#    real e(nn): the error for each value of n.  These must be strictly
#    positive, nonzero values.
#
#  Output:
#
#    real eoc(nn): the estimates for convergence order.  eoc(1) is not
#    defined, and is returned as NaN.
#
  import numpy as np

  nn = e.size

  eoc = np.zeros ( nn )

  for k in range ( 0, nn ):
    if ( k == 0 ):
      eoc[k] = np.NaN
    else:
      eoc[k] = np.log ( e[k-1] / e[k] ) / np.log ( n[k] / n[k-1] )

  return eoc

def convergence_n_test01 ( ):

#*****************************************************************************80
#
## convergence_n_test01() tests convergence_n() on a set of 7 results.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'convergence_n_test01():' )
  print ( '  A computation has been carried out with n=2^k intervals,' )
  print ( '  where n = 8, 16, ..., 512, and for each n, the' )
  print ( '  approximation error e(n) was computed.' )
  print ( '  convergence_n() estimates the convergence order.' )

  nn = 7
  n = np.array ( [ 8,        16,       32,       64,       128,      256,      512 ] )
  e = np.array ( [ 1.17e-02, 1.76e-04, 9.94e-05, 2.40e-06, 2.02e-07, 6.46e-09, 3.07e-10 ] )

  print ( '' )
  print ( '  The number of computations was ', nn )
  print ( '  The size n = 2^k was' )
  print ( n )
  print ( '  The errors e(n):' )
  print ( e )
#
#  Request convergence order estimates.
#
  eoc = convergence_n ( n, e )

  eoc_mean = np.mean ( eoc[1:] )

  print ( '' )
  print ( '    n(k)  error(k)   eoc(k)' )
  print ( '' )
  for k in range ( 0, nn ):
    print ( '  %3d  %.2e  %.2f' % ( n[k], e[k], eoc[k] ) )
  print ( '' )
  print ( '  eoc mean       %.2f' % ( eoc_mean ) )

  return

def convergence_n_test02 ( ):

#*****************************************************************************80
#
## convergence_n_test02() tests convergence_n() on a set of 6 results.
#
#  Discussion:
#
#    The solution method is presumable of order 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'convergence_n_test02():' )
  print ( '  A computation has been carried out with n=2^k intervals,' )
  print ( '  where n = 8, 16, ..., 512, and for each n, the' )
  print ( '  approximation error e(n) was computed.' )
  print ( '  convergence_n() estimates the convergence order.' )

  nn = 6
  n = np.array ( [ 4,           8,           16,          32,          64,          128 ] )
  e = np.array ( [ 6.05759e-05, 2.04755e-05, 5.66053e-06, 1.47327e-06, 3.74947e-07, 9.45143e-08 ] )

  print ( '' )
  print ( '  The number of computations was ', nn )
  print ( '  The size n = 2^k was' )
  print ( n )
  print ( '  The errors e(n):' )
  print ( e )
#
#  Request convergence order estimates.
#
  eoc = convergence_n ( n, e )

  eoc_mean = np.mean ( eoc[1:] )

  print ( '' )
  print ( '    n(k)  error(k)   eoc(k)' )
  print ( '' )
  for k in range ( 0, nn ):
    print ( '  %3d  %.2e  %.2f' % ( n[k], e[k], eoc[k] ) )
  print ( '' )
  print ( '  eoc mean       %.2f' % ( eoc_mean ) )

  return

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
  convergence_test ( )
  timestamp ( )

