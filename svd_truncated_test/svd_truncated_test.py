#! /usr/bin/env python3
#
def svd_truncated_test ( ):

#*****************************************************************************80
#
## svd_truncated_test() tests the truncated SVD factorization.
#
#  Discussion:
#
#    The standard SVD factorization of an MxN matrix A is:
#      A = U*S*V'
#    where U is MxM, S (diagonal) is MxN, and V' is NxN.
#
#    In fact, if M is much greater than N, we can write
#      A = U$ * S * V'
#    where U$ is MxN, S is NxN, and V' is NxN
#
#    and if M is much smaller than N, we can write
#      A = U * S * V$'
#    where U is MxM, S is MxM, and V$' is MxN.
#
#    When there is a great discrepancy between M and N, these
#    alternatives can save time and space.
#
#    MATLAB calls this the 'economy' SVD.
#    Python calls this the 'full_matrices=False' option.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'svd_truncated_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Demonstrate the use of the truncated' )
  print ( '  Singular Value Decomposition (SVD) for cases where' )
  print ( '  the sizes of M and N are very different.' )

  rng = default_rng ( )

  m = 4
  n = 3
  svd_truncated_u_test ( m, n, rng )

  m = 3
  n = 4
  svd_truncated_v_test ( m, n, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'svd_truncated_test():' )
  print ( '  Normal end of execution.' )

  return

def svd_truncated_u_test ( m, n, rng ):

#*****************************************************************************80
#
## svd_truncated_u_test() tests svd_truncated_u().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'svd_truncated_u_test():' )
  print ( '  M =', m )
  print ( '  N =', n )

  A = rng.random ( size = [ m, n ] )

  print ( '' )
  print ( '  Original matrix A:' )
  print ( A )

  Un, svec, V = np.linalg.svd ( A, full_matrices = False )
#
#  Build S.
#
  minmn = min ( m, n )
  S = np.zeros ( [ minmn, minmn ] )
  for i in range ( 0, minmn ):
    S[i,i] = svec[i]
#
#  Check the factorization by computing A = U * S * V'
#
  USV = np.dot ( Un, np.dot ( S, V ) )

  err = np.max ( np.abs ( A - USV ) )

  print ( '' )
  print ( '  Maximum error |A - U*S*V''| = ', err )
  print ( '' )
  print ( '  Recomputed A = U * S * V:' )
  print ( USV )

  return

def svd_truncated_v_test ( m, n, rng ):

#*****************************************************************************80
#
## svd_truncated_v_test() tests svd_truncated_v().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'svd_truncated_v_test():' )
  print ( '  M =', m )
  print ( '  N =', n )

  A = rng.random ( size = [ m, n ] )

  print ( '' )
  print ( '  Original matrix A:' )
  print ( A )

  U, svec, Vm = np.linalg.svd ( A, full_matrices = False )
#
#  Build S.
#
  minmn = min ( m, n )
  S = np.zeros ( [ minmn, minmn ] )
  for i in range ( 0, minmn ):
    S[i,i] = svec[i]
#
#  Check the factorization by computing A = U * S * V
#
  USV = np.dot ( U, np.dot ( S, Vm ) )

  err = np.max ( np.abs ( A - USV ) )

  print ( '' )
  print ( '  Maximum error |A - U*S*V''| = ', err )
  print ( '' )
  print ( '  Recomputed A = U * S * V'':' )
  print ( USV )

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
  svd_truncated_test ( )
  timestamp ( )


