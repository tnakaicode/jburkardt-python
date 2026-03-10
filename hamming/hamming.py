#! /usr/bin/env python3
#
def hamming74_g ( ):

#*****************************************************************************80
#
## hamming74_g() returns the Hamming (7,4) code generation matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real G(7,4), the Hamming (7,4) G matrix.
#
  import numpy as np

  g = np.array ( [ \
    [ 1, 1, 0, 1 ], \
    [ 1, 0, 1, 1 ], \
    [ 1, 0, 0, 0 ], \
    [ 0, 1, 1, 1 ], \
    [ 0, 1, 0, 0 ], \
    [ 0, 0, 1, 0 ], \
    [ 0, 0, 0, 1 ] ] )

  return g

def hamming74_g_test ( ):

#*****************************************************************************80
#
## hamming74_g_test() tests hamming74_g().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  r = 3
  n = 2**r - 1
  k = 2**r - r - 1

  print ( '' )
  print ( 'hamming74_g_test():' )
  print ( '  hamming74_g() returns the Hamming G74 matrix.' )
  print ( '  Multiplying a message by G74 gives the corresponding codeword.' )
  print ( '' )
  print ( '  Exponent R = ', r )
  print ( '  Block length N = 2**R-1 = ', n )
  print ( '  Message length K = 2**R - R - 1 = ', k )

  g74 = hamming74_g ( )

  print ( '' )
  print ( '   I Message(I)      Codeword(I)' )
  print ( '' )

  i_max = 2**k - 1

  for i in range ( 0, i_max + 1 ):
    x = ui4_to_ubvec ( i, k )
    y = np.dot ( g74, x )
    y = ( y % 2 )
    print ( '  ', i, ':', x[0:k], '-->', y[0:n] )

  return

def hamming74_h ( ):

#*****************************************************************************80
#
## hamming74_h() returns the Hamming (7,4) parity check matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real H(3,7), the Hamming (7,4) H matrix.
#
  import numpy as np

  h = np.array ( [ \
    [ 1, 0, 1, 0, 1, 0, 1 ], \
    [ 0, 1, 1, 0, 0, 1, 1 ], \
    [ 0, 0, 0, 1, 1, 1, 1 ] ] )

  return h

def hamming74_h_test ( ):

#*****************************************************************************80
#
## hamming74_h_test() tests hamming74_h().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  r = 3
  n = 2**r - 1
  k = 2**r - r - 1

  print ( '' )
  print ( 'hamming74_h_test():' )
  print ( '  hamming74_h() returns the Hamming H74 parity-check matrix.' )
  print ( '' )
  print ( '  Exponent R = ', r )
  print ( '  Block length N = 2**R-1 = ', n )
  print ( '  Message length K = 2**R - R - 1 = ', k )

  h74 = hamming74_h ( )
  g74 = hamming74_g ( )

  print ( '' )
  print ( '  Test #1: mod ( H * G, 2 ) = 0?' )
  print ( '' )

  hg = np.matmul ( h74, g74 )
  hg = ( hg % 2 )

  print ( '  | mod ( H * G, 2 ) | = ', np.linalg.norm ( hg, 'fro' ) )

  print ( '' )
  print ( '  Test #2: Only codewords with 0 parity are Messages' )
  print ( '' )

  print ( '' )
  print ( '    I   Codeword(I)         Parity' )
  print ( '' )

  i_max = 2**n - 1

  for i in range ( 0, i_max + 1 ):
    y = ui4_to_ubvec ( i, n )
    p = np.dot ( h74, y )
    p = ( p % 2 )
    print ( '  ', i, ':', y[0:n], '-->', p[0:k-1] )

  return

def hamming74_r ( ):

#*****************************************************************************80
#
## hamming74_r() returns the Hamming (7,4) decoding matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real R(4,7), the Hamming (7,4) R matrix.
#
  import numpy as np

  r = np.array ( [ \
    [ 0, 0, 1, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 0, 1, 0, 0 ], \
    [ 0, 0, 0, 0, 0, 1, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 1 ] ] )

  return r

def hamming74_r_test ( ):

#*****************************************************************************80
#
## hamming74_r_test() tests hamming74_r().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  r = 3
  n = 2**r - 1
  k = 2**r - r - 1

  print ( '' )
  print ( 'hamming74_r_test():' )
  print ( '  hamming74_r() returns the Hamming R74 matrix.' )
  print ( '  Multiplying a codeword by R74 gives the original message.' )
  print ( '' )
  print ( '  Exponent R = ', r )
  print ( '  Block length N = 2**R-1 = ', n )
  print ( '  Message length K = 2**R - R - 1 = ', k )

  g74 = hamming74_g ( )
  r74 = hamming74_r ( )

  print ( '' )
  print ( '   I   Message       Codeword            Message' )
  print ( '' )

  i_max = 2**k - 1

  for i in range ( 0, i_max + 1 ):
    x = ui4_to_ubvec ( i, k )
    y = np.dot ( g74, x )
    y = ( y % 2 )
    z = np.dot ( r74, y )
    print ( '  ', i, ':', x[0:k], '-->', y[0:n], '-->', z[0:k] )

  return

def hamming84_g ( ):

#*****************************************************************************80
#
## hamming84_g() returns the Hamming (8,4) code generation matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real G(8,4), the Hamming (8,4) G matrix.
#
  import numpy as np

  g = np.array ( [ \
    [ 1, 0, 0, 0 ], \
    [ 0, 1, 0, 0 ], \
    [ 0, 0, 1, 0 ], \
    [ 0, 0, 0, 1 ], \
    [ 0, 1, 1, 1 ], \
    [ 1, 0, 1, 1 ], \
    [ 1, 1, 0, 1 ], \
    [ 1, 1, 1, 0 ] ] )

  return g

def hamming84_g_test ( ):

#*****************************************************************************80
#
## hamming84_g_test() tests hamming84_g().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  r = 3
  n = 2**r
  k = 2**r - r - 1

  print ( '' )
  print ( 'hamming84_g_test():' )
  print ( '  hamming84_g() returns the Hamming G84 matrix.' )
  print ( '  Multiplying a message by G84 gives the corresponding codeword,' )
  print ( '  and includes a parity bit.' )
  print ( '' )
  print ( '  Exponent R = ', r )
  print ( '  Block length N = 2**R-1 = ', n )
  print ( '  Message length K = 2**R - R - 1 = ', k )

  g84 = hamming84_g ( )

  print ( '' )
  print ( '   I Message(I)      Codeword(I)' )
  print ( '' )

  i_max = 2**k - 1

  for i in range ( 0, i_max + 1 ):
    x = ui4_to_ubvec ( i, k )
    y = np.dot ( g84, x )
    y = ( y % 2 )
    print ( '  ', i, ':', x[0:k], '-->', y[0:n] )

  return

def hamming84_h ( ):

#*****************************************************************************80
#
## hamming84_h() returns the Hamming (8,4) parity check matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real H(4,8), the Hamming (8,4) H matrix.
#
  import numpy as np

  h = np.array ( [ \
    [ 0, 1, 1, 1, 1, 0, 0, 0 ], \
    [ 1, 0, 1, 1, 0, 1, 0, 0 ], \
    [ 1, 1, 0, 1, 0, 0, 1, 0 ], \
    [ 1, 1, 1, 0, 0, 0, 0, 1 ] ] )

  return h

def hamming84_h_test ( ):

#*****************************************************************************80
#
## hamming84_h_test() tests hamming74_h().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  r = 3
  n = 2**r
  k = 2**r - r - 1

  print ( '' )
  print ( 'hamming84_h_test():' )
  print ( '  hamming84_h() returns the Hamming H74 parity-check matrix.' )
  print ( '' )
  print ( '  Exponent R = ', r )
  print ( '  Block length N = 2**R = ', n )
  print ( '  Message length K = 2**R - R - 1 = ', k )

  h84 = hamming84_h ( )
  g84 = hamming84_g ( )

  print ( '' )
  print ( '  Test #1: mod ( H * G, 2 ) = 0?' )
  print ( '' )

  hg = np.matmul ( h84, g84 )
  hg = ( hg % 2 )

  print ( '  | mod ( H * G, 2 ) | = ', np.linalg.norm ( hg, 'fro' ) )

  print ( '' )
  print ( '  Test #2: Only codewords with 0 parity are Messages' )
  print ( '' )

  print ( '' )
  print ( '    I   Codeword(I)           Parity' )
  print ( '' )

  i_max = 2**n - 1

  for i in range ( 0, i_max + 1 ):
    y = ui4_to_ubvec ( i, n )
    p = np.dot ( h84, y )
    p = ( p % 2 )
    print ( '  ', i, ':', y[0:n], '-->', p[0:k] )

  return

def hamming84_r ( ):

#*****************************************************************************80
#
## hamming84_r() returns the Hamming (8,4) decoding matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real R(4,8), the Hamming (8,4) R matrix.
#
  import numpy as np

  r = np.array ( [ \
    [ 1, 0, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 1, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 0, 1, 0, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 1, 0, 0, 0, 0 ] ] )

  return r

def hamming84_r_test ( ):

#*****************************************************************************80
#
## hamming84_r_test() tests hamming84_r().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  r = 3
  n = 2**r
  k = 2**r - r - 1

  print ( '' )
  print ( 'hamming84_r_test():' )
  print ( '  hamming84_r() returns the Hamming R84 matrix.' )
  print ( '  Multiplying a codeword by R84 gives the original message.' )
  print ( '' )
  print ( '  Exponent R = ', r )
  print ( '  Block length N = 2**R = ', n )
  print ( '  Message length K = 2**R - R - 1 = ', k )

  g84 = hamming84_g ( )
  r84 = hamming84_r ( )

  print ( '' )
  print ( '   I   Message       Codeword              Message' )
  print ( '' )

  i_max = 2**k - 1

  for i in range ( 0, i_max + 1 ):
    x = ui4_to_ubvec ( i, k )
    y = np.dot ( g84, x )
    y = ( y % 2 )
    z = np.dot ( r84, y )
    print ( '  ', i, ':', x[0:k], '-->', y[0:n], '-->', z[0:k] )

  return

def hamming_test ( ):

#*****************************************************************************80
#
## hamming_test() tests hamming().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'hamming_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hamming()' )

  ui4_to_ubvec_test ( )

  hamming74_g_test ( )
  hamming74_h_test ( )
  hamming74_r_test ( )

  hamming84_g_test ( )
  hamming84_h_test ( )
  hamming84_r_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'hamming_test():' )
  print ( '  Normal end of execution.' )

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

def ubvec_to_ui4 ( n, ubvec ):

#*****************************************************************************80
#
## ubvec_to_ui4() makes an unsigned integer from an unsigned binary vector.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  UBVEC(1) is the units digit, UBVEC(N)
#    is the coefficient of 2**(N-1).
#
#  Example:
#
#    N = 4
#
#        UBVEC   binary  I
#    ----------  -----  --
#    1  2  3  4
#    ----------
#    1, 0, 0, 0       1  1
#    0, 1, 0, 0      10  2
#    0, 0, 1, 1      11  3
#    0, 0, 1, 0     100  4
#    1, 0, 0, 1    1001  9
#    1, 1, 1, 1    1111 15
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    integer UBVEC(N), the binary representation.
#
#  Output:
#
#    integer VALUE, the integer.
#
  value = 0
  for i in range ( 0, n ):
    value = 2 * value + ubvec[i]

  return value

def ubvec_to_ui4_test ( ):

#*****************************************************************************80
#
## ubvec_to_ui4_test() tests ubvec_to_ui4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'ubvec_to_ui4_test():' )
  print ( '  ubvec_to_ui4() converts an unsigned binary vector' )
  print ( '  to an unsigned integer' )
  print ( '' )
  print ( '  UI4 --> UBVEC  -->  UI4' )
  print ( '' )

  for ui4 in range ( 0, 11 ):
    ubvec = ui4_to_ubvec ( ui4, n )
    i2 = ubvec_to_ui4 ( n, ubvec )
    print ( '  %2d  ' % ( ui4 ), end = '' )
    for j in range ( 0, n ):
      print ( '%1d' % ( ubvec[j] ), end = '' )
    print ( '  %2d' % ( i2 ) )

  return

def ui4_to_ubvec ( ui4, n ):

#*****************************************************************************80
#
## ui4_to_ubvec() makes a unsigned binary vector from an integer.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  BVEC(1) is the units digit, BVEC(N)
#    is the coefficient of 2**(N-1).
#
#    To guarantee that there will be enough space for any
#    value of I, it would be necessary to set N = 32.
#
#  Example:
#
#     I       BVEC         binary
#    --  ----------------  ------
#     1  1, 0, 0, 0, 0, 0       1
#     2  0, 1, 0, 0, 0, 0      10
#     3  1, 1, 0, 0, 0, 0      11
#     4  0, 0, 1, 0, 0, 0     100
#     9  1, 0, 0, 1, 0, 0    1001
#    -9  1, 1, 1, 0, 1, 1  110111
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer UI4, an integer to be represented.
#
#    integer N, the dimension of the vector.
#
#  Output:
#
#    integer BVEC(N), the unsigned binary representation.
#
  import numpy as np

  ubvec = np.zeros ( n )

  for i in range ( n - 1, -1, -1 ):
    ubvec[i] = ( ui4 % 2 )
    ui4 = ( ui4 // 2 )

  return ubvec

def ui4_to_ubvec_test ( ):

#*****************************************************************************80
#
## ui4_to_ubvec_test() tests ui4_to_ubvec().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'ui4_to_ubvec_test():' )
  print ( '  ui4_to_ubvec() converts an unsigned integer to an' )
  print ( '  unsigned binary vector;' )
  print ( '' )
  print ( '  UI4 --> UBVEC  -->  UI4' )
  print ( '' )

  for i in range ( 0, 11 ):
    bvec = ui4_to_ubvec ( i, n )
    i2 = ubvec_to_ui4 ( n, bvec )
    print ( '  %2d  ' % ( i ), end = '' )
    for i in range ( 0, n ):
      print ( '%1d' % ( bvec[i] ), end = '' )
    print ( '  %2d' % ( i2 ) )

  return

if ( __name__ == "__main__" ):
  timestamp ( )
  hamming_test ( )
  timestamp ( )

