#! /usr/bin/env python3
#
def gamma_log_values ( n_data ):

#*****************************************************************************80
#
## GAMMA_LOG_VALUES returns some values of the Log Gamma function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Log[Gamma[x]]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
      0.1524063822430784E+01, \
      0.7966778177017837E+00, \
      0.3982338580692348E+00, \
      0.1520596783998375E+00, \
      0.0000000000000000E+00, \
     -0.4987244125983972E-01, \
     -0.8537409000331584E-01, \
     -0.1081748095078604E+00, \
     -0.1196129141723712E+00, \
     -0.1207822376352452E+00, \
     -0.1125917656967557E+00, \
     -0.9580769740706586E-01, \
     -0.7108387291437216E-01, \
     -0.3898427592308333E-01, \
     0.00000000000000000E+00, \
     0.69314718055994530E+00, \
     0.17917594692280550E+01, \
     0.12801827480081469E+02, \
     0.39339884187199494E+02, \
     0.71257038967168009E+02 ) )

  x_vec = np.array ( ( \
      0.20E+00, \
      0.40E+00, \
      0.60E+00, \
      0.80E+00, \
      1.00E+00, \
      1.10E+00, \
      1.20E+00, \
      1.30E+00, \
      1.40E+00, \
      1.50E+00, \
      1.60E+00, \
      1.70E+00, \
      1.80E+00, \
      1.90E+00, \
      2.00E+00, \
      3.00E+00, \
      4.00E+00, \
     10.00E+00, \
     20.00E+00, \
     30.00E+00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def gamma_log_values_test ( ):

#*****************************************************************************80
#
## GAMMA_LOG_VALUE_TEST demonstrates the use of GAMMA_LOG_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 February 2009
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'GAMMA_LOG_VALUES:' )
  print ( '  GAMMA_LOG_VALUES stores values of' )
  print ( '  the logarithm of the Gamma function.' )
  print ( '' )
  print ( '      X            GAMMA_LOG(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GAMMA_LOG_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p00_a ( prob, m, n ):

#*****************************************************************************80
#
## P00_A returns the matrix A for any least squares problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the problem index.
#
#    Input, integer M, the number of equations.
#
#    Input, integer N, the number of variables.
#
#    Output, real A(M,N), the matrix.
#
  from sys import exit

  if ( prob == 1 ):
    a = p01_a ( m, n )
  elif ( prob == 2 ):
    a = p02_a ( m, n )
  elif ( prob == 3 ):
    a = p03_a ( m, n )
  elif ( prob == 4 ):
    a = p04_a ( m, n )
  elif ( prob == 5 ):
    a = p05_a ( m, n )
  elif ( prob == 6 ):
    a = p06_a ( m, n )
  else:
    print ( '' )
    print ( 'P00_A - Fatal error!' )
    print ( '  Illegal value of PROB = %d' % ( prob ) )
    exit ( 'P00_A - Fatal error!' )

  return a

def p00_b ( prob, m ):

#*****************************************************************************80
#
## P00_B returns the right hand side B for any least squares problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the problem index.
#
#    Input, integer M, the number of equations.
#
#    Output, real B(M), the right hand side.
#
  from sys import exit

  if ( prob == 1 ):
    b = p01_b ( m )
  elif ( prob == 2 ):
    b = p02_b ( m )
  elif ( prob == 3 ):
    b = p03_b ( m )
  elif ( prob == 4 ):
    b = p04_b ( m )
  elif ( prob == 5 ):
    b = p05_b ( m )
  elif ( prob == 6 ):
    b = p06_b ( m )
  else:
    print ( '' )
    print ( 'P00_B - Fatal error!' )
    print ( '  Illegal value of PROB = %d' % ( prob ) )
    exit ( 'P00_B - Fatal error!' )

  return b

def p00_m ( prob ):

#*****************************************************************************80
#
## P00_M returns the number of equations M for any least squares problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the problem index.
#
#    Output, integer M, the number of equations.
#
  from sys import exit

  if ( prob == 1 ):
    m = p01_m ( )
  elif ( prob == 2 ):
    m = p02_m ( )
  elif ( prob == 3 ):
    m = p03_m ( )
  elif ( prob == 4 ):
    m = p04_m ( )
  elif ( prob == 5 ):
    m = p05_m ( )
  elif ( prob == 6 ):
    m = p06_m ( )
  else:
    print ( '' )
    print ( 'P00_M - Fatal error!' )
    print ( '  Illegal value of PROB = %d' % ( prob ) )
    exit ( 'P00_M - Fatal error!' )

  return m

def p00_n ( prob ):

#*****************************************************************************80
#
## P00_N returns the number of variables N for any least squares problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the problem index.
#
#    Output, integer N, the number of variables.
#
  from sys import exit

  if ( prob == 1 ):
    n = p01_n ( )
  elif ( prob == 2 ):
    n = p02_n ( )
  elif ( prob == 3 ):
    n = p03_n ( )
  elif ( prob == 4 ):
    n = p04_n ( )
  elif ( prob == 5 ):
    n = p05_n ( )
  elif ( prob == 6 ):
    n = p06_n ( )
  else:
    print ( '' )
    print ( 'P00_N - Fatal error!' )
    print ( '  Illegal value of PROB = %d' % ( prob ) )
    exit ( 'P00_N - Fatal error!' )

  return n

def p00_prob_num ( ):

#*****************************************************************************80
#
## P00_PROB_NUM returns the number of least squares problems.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real PROB_NUM, the number of problems.
#
  prob_num = 6

  return prob_num

def p00_x ( prob, n ):

#*****************************************************************************80
#
## P00_X returns the least squares solution X for any least squares problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the problem index.
#
#    Input, integer N, the number of variables.
#
#    Output, real X(N), the least squares solution.
#
  from sys import exit

  if ( prob == 1 ):
    x = p01_x ( n )
  elif ( prob == 2 ):
    x = p02_x ( n )
  elif ( prob == 3 ):
    x = p03_x ( n )
  elif ( prob == 4 ):
    x = p04_x ( n )
  elif ( prob == 5 ):
    x = p05_x ( n )
  elif ( prob == 6 ):
    x = p06_x ( n )
  else:
    print ( '' )
    print ( 'P00_X - Fatal error!' )
    print ( '  Illegal value of PROB = %d' % ( prob ) )
    exit ( 'P00_X - Fatal error!' )

  return x

def p01_a ( m, n ):

#*****************************************************************************80
#
## P01_A returns the matrix A for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of equations.
#
#    Input, integer N, the number of variables.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    a[i,0] = 1.0
    for j in range ( 1, n ):
      a[i,j] = a[i,j-1] * float ( i + 1 )

  return a

def p01_b ( m ):

#*****************************************************************************80
#
## P01_B returns the right hand side B for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of equations.
#
#    Output, real B(M), the right hand side.
#
  import numpy as np

  b = np.array ( [ 1.0, 2.3, 4.6, 3.1, 1.2 ] )

  return b

def p01_m ( ):

#*****************************************************************************80
#
## P01_M returns the number of equations M for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer M, the number of equations.
#
  m = 5

  return m

def p01_n ( ):

#*****************************************************************************80
#
## P01_N returns the number of variables N for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer N, the number of variables.
#
  n = 3

  return n

def p01_x ( n ):

#*****************************************************************************80
#
## P01_X returns the least squares solution X for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of variables.
#
#    Output, real X(N), the least squares solution.
#
  import numpy as np

  x = np.array ( [ -3.0200000, 4.4914286, -0.72857143 ] )

  return x

def p02_a ( m, n ):

#*****************************************************************************80
#
## P02_A returns the matrix A for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625,
#    ebook: http://www.mathworks.com/moler/chapters.html
#
#  Parameters:
#
#    Input, integer M, the number of equations.
#
#    Input, integer N, the number of variables.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    a[i,n-1] = 1.0
    for j in range ( n - 2, -1, -1 ):
      a[i,j] = a[i,j+1] * float ( i ) / 5.0

  return a

def p02_b ( m ):

#*****************************************************************************80
#
## P02_B returns the right hand side B for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of equations.
#
#    Output, real B(M), the right hand side.
#
  import numpy as np

  b = np.array ( [ 150.697, 179.323, 203.212, 226.505, 249.633, 281.422 ] )

  return b

def p02_m ( ):

#*****************************************************************************80
#
## P02_M returns the number of equations M for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer M, the number of equations.
#
  m = 6

  return m

def p02_n ( ):

#*****************************************************************************80
#
## P02_N returns the number of variables N for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer N, the number of variables.
#
  n = 3

  return n

def p02_x ( n ):

#*****************************************************************************80
#
## P02_X returns the least squares solution X for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of variables.
#
#    Output, real X(N), the least squares solution.
#
  import numpy as np

  x = np.array ( [ 5.7013, 121.1341, 152.4745 ] )

  return x

def p03_a ( m, n ):

#*****************************************************************************80
#
## P03_A returns the matrix A for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625,
#    ebook: http://www.mathworks.com/moler/chapters.html
#
#  Parameters:
#
#    Input, integer M, the number of equations.
#
#    Input, integer N, the number of variables.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  a = np.array ( [ \
       [  1.0,  2.0,  3.0 ], \
       [  4.0,  5.0,  6.0 ], \
       [  7.0,  8.0,  9.0 ], \
       [ 10.0, 11.0, 12.0 ], \
       [ 13.0, 14.0, 15.0 ] ] )

  return a

def p03_b ( m ):

#*****************************************************************************80
#
## P03_B returns the right hand side B for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of equations.
#
#    Output, real B(M), the right hand side.
#
  import numpy as np

  b = np.array ( [ 16.0, 17.0, 18.0, 19.0, 20.0 ] )

  return b

def p03_m ( ):

#*****************************************************************************80
#
## P03_M returns the number of equations M for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer M, the number of equations.
#
  m = 5

  return m

def p03_n ( ):

#*****************************************************************************80
#
## P03_N returns the number of variables N for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer N, the number of variables.
#
  n = 3

  return n

def p03_x ( n ):

#*****************************************************************************80
#
## P03_X returns the least squares solution X for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of variables.
#
#    Output, real X(N), the least squares solution.
#
  import numpy as np

  x = np.array ( [ -7.5555556, 0.1111111, 7.7777778 ] )

  return x

def p04_a ( m, n ):

#*****************************************************************************80
#
## P04_A returns the matrix A for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of equations.
#
#    Input, integer N, the number of variables.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = float ( j + 1 ) ** i

  return a

def p04_b ( m ):

#*****************************************************************************80
#
## P04_B returns the right hand side B for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of equations.
#
#    Output, real B(M), the right hand side.
#
  import numpy as np

  b = np.array ( [ 15.0, 55.0, 225.0 ] )

  return b

def p04_m ( ):

#*****************************************************************************80
#
## P04_M returns the number of equations M for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer M, the number of equations.
#
  m = 3

  return m

def p04_n ( ):

#*****************************************************************************80
#
## P04_N returns the number of variables N for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer N, the number of variables.
#
  n = 5

  return n

def p04_x ( n ):

#*****************************************************************************80
#
## P04_X returns the least squares solution X for problem 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of variables.
#
#    Output, real X(N), the least squares solution.
#
  import numpy as np

  x = np.array ( [ 1.0, 2.0, 3.0, 4.0, 5.0 ] )

  return x

def p05_a ( m, n ):

#*****************************************************************************80
#
## P05_A returns the matrix A for problem 5.
#
#  Discussion:
#
#    A is the Hilbert matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of equations.
#
#    Input, integer N, the number of variables.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = 1.0 / float ( i + j + 1 )

  return a

def p05_b ( m ):

#*****************************************************************************80
#
## P05_B returns the right hand side B for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of equations.
#
#    Output, real B(M), the right hand side.
#
  import numpy as np

  b = np.zeros ( m )

  b[0] = 1.0

  return b

def p05_m ( ):

#*****************************************************************************80
#
## P05_M returns the number of equations M for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer M, the number of equations.
#
  m = 10

  return m

def p05_n ( ):

#*****************************************************************************80
#
## P05_N returns the number of variables N for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer N, the number of variables.
#
  n = 10

  return n

def p05_x ( n ):

#*****************************************************************************80
#
## P05_X returns the least squares solution X for problem 5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of variables.
#
#    Output, real X(N), the least squares solution.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = r8_mop ( i + 2 ) * float ( i + 1 ) \
      * r8_choose ( n + i, n - 1 ) * r8_choose ( n, n - i - 1 )

  return x

def p06_a ( m, n ):

#*****************************************************************************80
#
## P06_A returns the matrix A for problem 6.
#
#  Discussion:
#
#    A is a symmetric, orthogonal matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of equations.
#
#    Input, integer N, the number of variables.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      angle = float ( i + 1 ) * float ( j + 1 ) * np.pi / float ( n + 1 )
      a[i,j] = np.sin ( angle )

  a[0:m,0:n] = a[0:m,0:n] * np.sqrt ( 2.0 / ( n + 1 ) )

  return a

def p06_b ( m ):

#*****************************************************************************80
#
## P06_B returns the right hand side B for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of equations.
#
#    Output, real B(M), the right hand side.
#
  import numpy as np

  b = np.zeros ( m )

  b[0] = 1.0

  return b

def p06_m ( ):

#*****************************************************************************80
#
## P06_M returns the number of equations M for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer M, the number of equations.
#
  m = 10

  return m

def p06_n ( ):

#*****************************************************************************80
#
## P06_N returns the number of variables N for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer N, the number of variables.
#
  n = 10

  return n

def p06_x ( n ):

#*****************************************************************************80
#
## P06_X returns the least squares solution X for problem 6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of variables.
#
#    Output, real X(N), the least squares solution.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( n + 1 )
    x[i] = np.sin ( angle )

  x[0:n] = x[0:n] * np.sqrt ( 2.0 / float ( n + 1) )

  return x

def r8_choose ( n, k ):

#*****************************************************************************80
#
## R8_CHOOSE computes the binomial coefficient C(N,K) as an R8.
#
#  Discussion:
#
#    The value is calculated in such a way as to avoid overflow and
#    roundoff.  The calculation is done in R8 arithmetic.
#
#    The formula used is:
#
#      C(N,K) = N! / ( K! * (N-K)! )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, K, are the values of N and K.
#
#    Output, real VALUE, the number of combinations of N
#    things taken K at a time.
#
  import numpy as np

  if ( n < 0 ):

    value = 0.0

  elif ( k == 0 ):

    value = 1.0

  elif ( k == 1 ):

    value = float ( n )

  elif ( 1 < k and k < n - 1 ):

    facn = r8_gamma_log ( float ( n + 1 ) )
    fack = r8_gamma_log ( float ( k + 1 ) )
    facnmk = r8_gamma_log ( float ( n - k + 1 ) )

    value = round ( np.exp ( facn - fack - facnmk ) )

  elif ( k == n - 1 ):

    value = float ( n )

  elif ( k == n ):

    value = 1.0

  else:

    value = 0.0

  return value

def r8_choose_test ( ):

#*****************************************************************************80
#
## R8_CHOOSE_TEST tests R8_CHOOSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8_CHOOSE_TEST' )
  print ( '  R8_CHOOSE evaluates C(N,K).' )
  print ( '' )
  print ( '         N         K       CNK' )
 
  for n in range ( 0, 6 ):
    print ( '' )
    for k in range ( 0, n + 1 ):
      cnk = r8_choose ( n, k )
      print ( '  %8d  %8d  %14.6g' % ( n, k, cnk ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_CHOOSE_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_gamma_log ( x ):

#*****************************************************************************80
#
## R8_GAMMA_LOG evaluates the logarithm of the gamma function.
#
#  Discussion:
#
#    This routine calculates the LOG(GAMMA) function for a positive real
#    argument X.  Computation is based on an algorithm outlined in
#    references 1 and 2.  The program uses rational functions that
#    theoretically approximate LOG(GAMMA) to at least 18 significant
#    decimal digits.  The approximation for X > 12 is from reference
#    3, while approximations for X < 12.0 are similar to those in
#    reference 1, but are unpublished.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    Original FORTRAN77 version by William Cody, Laura Stoltz.
#    PYTHON version by John Burkardt.
#
#  Reference:
#
#    William Cody, Kenneth Hillstrom,
#    Chebyshev Approximations for the Natural Logarithm of the
#    Gamma Function,
#    Mathematics of Computation,
#    Volume 21, Number 98, April 1967, pages 198-203.
#
#    Kenneth Hillstrom,
#    ANL/AMD Program ANLC366S, DGAMMA/DLGAMA,
#    May 1969.
#
#    John Hart, Ward Cheney, Charles Lawson, Hans Maehly,
#    Charles Mesztenyi, John Rice, Henry Thatcher,
#    Christoph Witzgall,
#    Computer Approximations,
#    Wiley, 1968,
#    LC: QA297.C64.
#
#  Parameters:
#
#    Input, real X, the argument of the function.
#
#    Output, real R8_GAMMA_LOG, the value of the function.
#
  import numpy as np
  from math import log

  c = np.array ( [ \
    -1.910444077728E-03, \
     8.4171387781295E-04, \
    -5.952379913043012E-04, \
     7.93650793500350248E-04, \
    -2.777777777777681622553E-03, \
     8.333333333333333331554247E-02, \
     5.7083835261E-03 ] )
  d1 = -5.772156649015328605195174E-01
  d2 = 4.227843350984671393993777E-01
  d4 = 1.791759469228055000094023E+00
  frtbig = 2.25E+76
  p1 = np.array ( [ \
    4.945235359296727046734888E+00, \
    2.018112620856775083915565E+02, \
    2.290838373831346393026739E+03, \
    1.131967205903380828685045E+04, \
    2.855724635671635335736389E+04, \
    3.848496228443793359990269E+04, \
    2.637748787624195437963534E+04, \
    7.225813979700288197698961E+03 ] )
  p2 = np.array ( [ \
    4.974607845568932035012064E+00, \
    5.424138599891070494101986E+02, \
    1.550693864978364947665077E+04, \
    1.847932904445632425417223E+05, \
    1.088204769468828767498470E+06, \
    3.338152967987029735917223E+06, \
    5.106661678927352456275255E+06, \
    3.074109054850539556250927E+06 ] )
  p4 = np.array ( [ \
    1.474502166059939948905062E+04, \
    2.426813369486704502836312E+06, \
    1.214755574045093227939592E+08, \
    2.663432449630976949898078E+09, \
    2.940378956634553899906876E+10, \
    1.702665737765398868392998E+11, \
    4.926125793377430887588120E+11, \
    5.606251856223951465078242E+11 ] )
  q1 = np.array ( [ \
    6.748212550303777196073036E+01, \
    1.113332393857199323513008E+03, \
    7.738757056935398733233834E+03, \
    2.763987074403340708898585E+04, \
    5.499310206226157329794414E+04, \
    6.161122180066002127833352E+04, \
    3.635127591501940507276287E+04, \
    8.785536302431013170870835E+03 ] )
  q2 = np.array ( [ \
    1.830328399370592604055942E+02, \
    7.765049321445005871323047E+03, \
    1.331903827966074194402448E+05, \
    1.136705821321969608938755E+06, \
    5.267964117437946917577538E+06, \
    1.346701454311101692290052E+07, \
    1.782736530353274213975932E+07, \
    9.533095591844353613395747E+06 ] )
  q4 = np.array ( [ \
    2.690530175870899333379843E+03, \
    6.393885654300092398984238E+05, \
    4.135599930241388052042842E+07, \
    1.120872109616147941376570E+09, \
    1.488613728678813811542398E+10, \
    1.016803586272438228077304E+11, \
    3.417476345507377132798597E+11, \
    4.463158187419713286462081E+11 ] )
  r8_epsilon = 2.220446049250313E-016
  sqrtpi = 0.9189385332046727417803297
  xbig = 2.55E+305
  xinf = 1.79E+308

  y = x

  if ( 0.0 < y and y <= xbig ):

    if ( y <= r8_epsilon ):

      res = - log ( y )
#
#  EPS < X <= 1.5.
#
    elif ( y <= 1.5 ):

      if ( y < 0.6796875 ):
        corr = -log ( y );
        xm1 = y;
      else:
        corr = 0.0;
        xm1 = ( y - 0.5 ) - 0.5;

      if ( y <= 0.5 or 0.6796875 <= y ):

        xden = 1.0;
        xnum = 0.0;
        for i in range ( 0, 8 ):
          xnum = xnum * xm1 + p1[i]
          xden = xden * xm1 + q1[i]

        res = corr + ( xm1 * ( d1 + xm1 * ( xnum / xden ) ) )

      else:

        xm2 = ( y - 0.5 ) - 0.5
        xden = 1.0
        xnum = 0.0
        for i in range ( 0, 8 ):
          xnum = xnum * xm2 + p2[i]
          xden = xden * xm2 + q2[i]

        res = corr + xm2 * ( d2 + xm2 * ( xnum / xden ) )
#
#  1.5 < X <= 4.0.
#
    elif ( y <= 4.0 ):

      xm2 = y - 2.0
      xden = 1.0
      xnum = 0.0
      for i in range ( 0, 8 ):
        xnum = xnum * xm2 + p2[i]
        xden = xden * xm2 + q2[i]

      res = xm2 * ( d2 + xm2 * ( xnum / xden ) )
#
#  4.0 < X <= 12.0.
#
    elif ( y <= 12.0 ):

      xm4 = y - 4.0
      xden = -1.0
      xnum = 0.0
      for i in range ( 0, 8 ):
        xnum = xnum * xm4 + p4[i]
        xden = xden * xm4 + q4[i]

      res = d4 + xm4 * ( xnum / xden )
#
#  Evaluate for 12 <= argument.
#
    else:

      res = 0.0

      if ( y <= frtbig ):

        res = c[6]
        ysq = y * y

        for i in range ( 0, 6 ):
          res = res / ysq + c[i]

      res = res / y
      corr = log ( y )
      res = res + sqrtpi - 0.5 * corr
      res = res + y * ( corr - 1.0 )
#
#  Return for bad arguments.
#
  else:

    res = xinf

  return res

def r8_gamma_log_test ( ):

#*****************************************************************************80
#
## R8_GAMMA_LOG_TEST tests R8_GAMMA_LOG.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8_GAMMA_LOG_TEST:' )
  print ( '  R8_GAMMA_LOG evaluates the logarithm of the Gamma function.' )
  print ( '' )
  print ( '      X            GAMMA_LOG(X)    R8_GAMMA_LOG(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_gamma_log ( x )

    print ( '  %12g  %24.16g  %24.16g' % ( x, fx1, fx2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_GAMMA_LOG_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_mop ( i ):

#*****************************************************************************80
#
## R8_MOP returns the I-th power of -1 as an R8 value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the power of -1.
#
#    Output, real R8_MOP, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1.0
  else:
    value = - 1.0

  return value

def r8_mop_test ( ):

#*****************************************************************************80
#
## R8_MOP_TEST tests R8_MOP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  from i4_uniform_ab import i4_uniform_ab

  print ( '' )
  print ( 'R8_MOP_TEST' )
  print ( '  R8_MOP evaluates (-1.0)^I4 as an R8.' )
  print ( '' )
  print ( '    I4  R8_MOP(I4)' )
  print ( '' )

  i4_min = -100;
  i4_max = +100;
  seed = 123456789;

  for test in range ( 0, 10 ):
    i4, seed = i4_uniform_ab ( i4_min, i4_max, seed )
    r8 = r8_mop ( i4 )
    print ( '  %4d  %4.1f' % ( i4, r8 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_MOP_TEST' )
  print ( '  Normal end of execution.' )
  return

def test_lls_test ( ):

#*****************************************************************************80
#
## TEST_LLS_TEST tests the TEST_LLS library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'TEST_LLS_TEST' )
  print ( '  Python version.' )
  print ( '  Test the TEST_LLS library.' )

  ls_data_test ( )
  lstsq_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TEST_LLS_TEST' )
  print ( '  Normal end of execution.' )
  return

def lstsq_test ( ):

#*****************************************************************************80
#
## LSTSQ_TEST tries out the NUMPY LINALG least squares solver on the data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'LSTSQ_TEST' )
  print ( '  LSTSQ is the NUMPY LINALG least squares solver.' )

  prob_num = p00_prob_num ( )

  print ( '' )
  print ( '  Number of problems = %d' % ( prob_num ) )
  print ( '' )
  print ( '  Index     M     N         ||B||     ||X1-X2||         ||X1|| ', end = '' )
  print ( '       ||X2||        ||R1||        ||R2||' )
  print ( '' )

  for prob in range ( 1, prob_num ):

    m = p00_m ( prob )
    n = p00_n ( prob )

    a = p00_a ( prob, m, n )
    b = p00_b ( prob, m )
    x1 = p00_x ( prob, n )

    r1 = np.dot ( a, x1 ) - b

    b_norm = np.linalg.norm ( b )
    x1_norm = np.linalg.norm ( x1 )
    r1_norm = np.linalg.norm ( r1 )

    [ x2, resids, rank, s ] = np.linalg.lstsq ( a, b, rcond = None )
    r2 = np.dot ( a, x2 ) - b
    x2_norm = np.linalg.norm ( x2 )
    r2_norm = np.linalg.norm ( r2 )

    x_diff_norm = np.linalg.norm ( x1 - x2 )

    print ( '  %5d  %4d  %4d  %12.4g  %12.4g  %12.4g  %12.4g  %12.4g  %12.4g' \
      % ( prob, m, n, b_norm, x_diff_norm, x1_norm, x2_norm, r1_norm, r2_norm ) )

  return

def ls_data_test ( ):

#*****************************************************************************80
#
## LS_DATA_TEST summarizes the test data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'LS_DATA_TEST' )
  print ( '  Get each least squares test and compute the maximum residual.' )
  print ( '  The L2 norm of the residual MUST be no greater than' )
  print ( '  the L2 norm of the right hand side, else 0 is a better solution.' )

  prob_num = p00_prob_num ( )

  print ( '' )
  print ( '  Number of problems = %d' % ( prob_num ) )
  print ( '' )
  print ( '  Index     M     N         ||B||         ||X||         ||R||' )
  print ( '' )

  for prob in range ( 1, prob_num + 1 ):

    m = p00_m ( prob )
    n = p00_n ( prob )

    a = p00_a ( prob, m, n )
    b = p00_b ( prob, m )
    x = p00_x ( prob, n )

    r = np.dot ( a, x ) - b

    b_norm = np.linalg.norm ( b )
    x_norm = np.linalg.norm ( x )
    r_norm = np.linalg.norm ( r )

    print ( '  %5d  %4d  %4d  %12.4g  %12.4g  %12.4g' \
      % ( prob, m, n, b_norm, x_norm, r_norm ) )

  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
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

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
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

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  test_lls_test ( )
  timestamp ( )

