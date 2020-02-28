#! /usr/bin/env python3
#
def mxm ( a, b, l, m, n ):

#*****************************************************************************80
#
## MXM computes the matrix product C = A * B.
#
#  Discussion:
#
#    The function uses 4-way unrolled loops to carry out matrix multiplication.
#
#    M must be a multiple of 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 July 2015
#
#  Author:
#
#    Original FORTRAN77 version by David Bailey.
#    Python version by John Burkardt.
#
  import numpy as np

  c = np.dot ( a, b )

  return c

def mxm_test ( ):

#*****************************************************************************80
#
## MXM_TEST tests MXM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 July 2015
#
#  Author:
#
#    Original FORTRAN77 version by David Bailey.
#    Python version by John Burkardt.
#
  import numpy as np
  from time import clock

  l = 256
  m = 128
  n = 64

  it = 100
  ans = 35.2026179738722
#
#  Random initialization.
#
  f7 = 78125.0
  t30 = 1073741824.0
  t = f7 / t30

  a = np.zeros ( [ l, m ] )
  for j in range ( 0, m ):
    for i in range ( 0, l ):
      t = ( ( f7 * t ) % 1.0 )
      a[i,j] = t

  b = np.zeros ( [ m, n ] )
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      t = ( ( f7 * t ) % 1.0 )
      b[i,j] = t
#
#  Timing.
#
  tm = clock ( )

  for ii in range ( 0, it ):
    c = mxm ( a, b, l, m, n )

  tm = clock ( ) - tm
#
#  Results.
#
  er = abs ( ( c[18,18] - ans ) / ans )
  fp = 2 * it * l * m * n
  rt = 1.0E-06 * fp / tm
#
#  Terminate.
#
  return er, fp, tm, rt

if ( __name__ == '__main__' ):
  import platform
  from timestamp import timestamp
  timestamp ( )
  er, fp, tm, rt = mxm_test ( )
  print ( '' )
  print ( 'MXM:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '' )
  print ( ' Program        Error          FP Ops        Seconds     MFLOPS' )
  print ( '' )
  print ( ' MXM      %13.4e  %13.4e  %10.4e  %10.2e' % ( er, fp, tm, rt ) )
  print ( '' )
  print ( 'MXM:' )
  print ( '  Normal end of execution.' )
  timestamp ( )

