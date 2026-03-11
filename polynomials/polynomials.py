#! /usr/bin/env python3
#
def butcher_b ( m ):

#*****************************************************************************80
#
## butcher_b() returns the bounds in the Butcher problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -1.0, -0.1, -0.1, -1.0, -0.1,  -0.1 ] )
  u = np.array ( [  0.0, +0.9, +0.5, -0.1, -0.05, -0.003] )

  return l, u

def butcher_f ( m, n, x ):

#*****************************************************************************80
#
## butcher_f() returns the function in the Butcher problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
      x[5,0:n] * x[1,0:n] ** 2 \
    + x[4,0:n] * x[2,0:n] ** 2 \
    - x[0,0:n] * x[3,0:n] ** 2 \
    + x[3,0:n] ** 3 \
    + x[3,0:n] ** 2 \
    - 1.0 / 3.0 * x[0,0:n] \
    + 4.0 / 3.0 * x[3,0:n]  )
 
  return value

def butcher_m ( ):

#*****************************************************************************80
#
## butcher_m() returns the number of variables in the Butcher problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 6

  return m

def butcher_test ( ):

#*****************************************************************************80
#
## butcher_test() uses sampling to estimate the range of the Butcher polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'butcher_test():' )
  print ( '  Use N sample values of the Butcher polynomial' )
  print ( '  to estimate its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = butcher_m ( )
  l, u = butcher_b ( m )
  print ( '  butcher: [-1.4393333333, +0.219]' )
  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = butcher_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def camel_b ( m ):

#*****************************************************************************80
#
## camel_b() returns the bounds in the camel problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -3.0, -3.0 ] )
  u = np.array ( [ +3.0, +3.0 ] )

  return l, u

def camel_f ( m, n, x ):

#*****************************************************************************80
#
## camel_f() returns the function in the camel problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
      4.0       * x[0,0:n] ** 2             \
    - 2.1       * x[0,0:n] ** 4             \
    + 1.0 / 3.0 * x[0,0:n] ** 6             \
    +             x[0,0:n]       * x[1,0:n] \
    - 4.0       * x[1,0:n] ** 2             \
    + 4.0       * x[1,0:n] ** 4 )

  return value

def camel_m ( ):

#*****************************************************************************80
#
## camel_m() returns the number of variables in the camel problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 2

  return m

def camel_test ( ):

#*****************************************************************************80
#
## camel_test() uses sampling to estimate the range of the CAMEL polynomial.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 January 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'camel_test():' )
  print ( '  Use N sample values of the Camel polyomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = camel_m ( )
  l, u = camel_b ( m )
  print ( '  camel: [ -1.031628453489616, ? ]:' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = camel_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def camera_b ( m ):

#*****************************************************************************80
#
## camera_b() returns the bounds in the camera problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -100.0, -100.0, -100.0, -100.0, -100.0, -100.0 ] )
  u = np.array ( [ +100.0, +100.0, +100.0, +100.0, +100.0, +100.0 ] )

  return l, u

def camera_f ( m, n, x ):

#*****************************************************************************80
#
## camera_f() returns the function in the camera problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
    - 6.8 * x[0,0:n] * x[3,0:n] \
    - 3.2 * x[0,0:n] * x[4,0:n] \
    + 1.3 * x[0,0:n] * x[5,0:n] \
    + 5.1 * x[0,0:n]             \
    - 3.2 * x[1,0:n] * x[3,0:n] \
    - 4.8 * x[1,0:n] * x[4,0:n] \
    - 0.7 * x[1,0:n] * x[5,0:n] \
    - 7.1 * x[1,0:n]             \
    + 1.3 * x[2,0:n] * x[3,0:n] \
    - 0.7 * x[2,0:n] * x[4,0:n] \
    + 9.0 * x[2,0:n] * x[5,0:n] \
    -       x[2,0:n] \
    + 5.1 * x[3,0:n] \
    - 7.1 * x[4,0:n] \
    -       x[5,0:n] \
    + 2.6 )

  return value

def camera_m ( ):

#*****************************************************************************80
#
## camera_m() returns the number of variables in the camera problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 6

  return m

def camera_test ( ):

#*****************************************************************************80
#
## camera_test() uses sampling to estimate the range of the CAMERA polynomial.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'camera_test():' )
  print ( '  Use N sample values of the Camera polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = camera_m ( )
  l, u = camera_b ( m )
  print ( '  camera: [-270397.4, +270202.6]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = camera_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def caprasse_b ( m ):

#*****************************************************************************80
#
## caprasse_b() returns the bounds in the caprasse problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -0.5, -0.5, -0.5, -0.5 ] )
  u = np.array ( [ +0.5, +0.5, +0.5, +0.5 ] )

  return l, u

def caprasse_f ( m, n, x ):

#*****************************************************************************80
#
## caprasse_f() returns the function in the caprasse problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
    -        x[0,0:n]       * x[2,0:n] ** 3                 \
    +  4.0 * x[1,0:n]       * x[2,0:n] ** 2 * x[3,0:n]      \
    +  4.0 * x[0,0:n]       * x[2,0:n]      * x[3,0:n] ** 2 \
    +  2.0 * x[1,0:n]       * x[3,0:n] ** 3                 \
    +  4.0 * x[0,0:n]       * x[2,0:n]                      \
    +  4.0 * x[2,0:n] ** 2                                  \
    - 10.0 * x[1,0:n]       * x[3,0:n]                      \
    - 10.0 * x[3,0:n] ** 2                                  \
    +  2.0 )

  return value

def caprasse_m ( ):

#*****************************************************************************80
#
## caprasse_m() returns the number of variables in the caprasse problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 4

  return m

def caprasse_test ( ):

#*****************************************************************************80
#
## caprasse_test() uses sampling to estimate the range of the CAPRASSE polynomial.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 January 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'caprasse_test():' )
  print ( '  Use N sample values of the Caprasse polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = caprasse_m ( )
  l, u = caprasse_b ( m )
  print ( '  caprasse: [-3.1800966258, +4.4852773332]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = caprasse_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def cyclic5_b ( m ):

#*****************************************************************************80
#
## cyclic5_b() returns the bounds in the cyclic5 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -10.0, -10.0, -10.0, -10.0, -10.0 ] )
  u = np.array ( [ +10.0, +10.0, +10.0, +10.0, +10.0 ] )

  return l, u

def cyclic5_f ( m, n, x ):

#*****************************************************************************80
#
## cyclic5_f() returns the function in the cyclic5 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
      x[0,0:n] * x[1,0:n] * x[2,0:n] * x[3,0:n] \
    + x[0,0:n] * x[1,0:n] * x[2,0:n] * x[4,0:n] \
    + x[0,0:n] * x[1,0:n] * x[3,0:n] * x[4,0:n] \
    + x[0,0:n] * x[2,0:n] * x[3,0:n] * x[4,0:n] \
    + x[1,0:n] * x[2,0:n] * x[3,0:n] * x[4,0:n] )

  return value

def cyclic5_m ( ):

#*****************************************************************************80
#
## cyclic5_m() returns the number of variables in the cyclic5 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 5

  return m

def cyclic5_test ( ):

#*****************************************************************************80
#
## cyclic5_test() uses sampling to estimate the range of the CYCLIC5 polynomial.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'cyclic5_test():' )
  print ( '  Use N sample values of the Cyclic5 polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = cyclic5_m ( )
  l, u = cyclic5_b ( m )
  print ( '  cyclic5: [-30000, +50000]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = cyclic5_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def cyclic7_b ( m ):

#*****************************************************************************80
#
## cyclic7_b() returns the bounds in the cyclic7 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0 ] )
  u = np.array ( [ +1.0, +1.0, +1.0, +1.0, +1.0, +1.0, +1.0 ] )

  return l, u

def cyclic7_f ( m, n, x ):

#*****************************************************************************80
#
## cyclic7_f() returns the function in the cyclic7 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
      x[0,0:n] * x[1,0:n] * x[2,0:n] * x[3,0:n] * x[4,0:n] * x[5,0:n]            \
    + x[0,0:n] * x[1,0:n] * x[2,0:n] * x[3,0:n] * x[4,0:n]            * x[6,0:n] \
    + x[0,0:n] * x[1,0:n] * x[2,0:n] * x[3,0:n]            * x[5,0:n] * x[6,0:n] \
    + x[0,0:n] * x[1,0:n] * x[2,0:n]            * x[4,0:n] * x[5,0:n] * x[6,0:n] \
    + x[0,0:n] * x[1,0:n]            * x[3,0:n] * x[4,0:n] * x[5,0:n] * x[6,0:n] \
    + x[0,0:n]            * x[2,0:n] * x[3,0:n] * x[4,0:n] * x[5,0:n] * x[6,0:n] \
    +            x[1,0:n] * x[2,0:n] * x[3,0:n] * x[4,0:n] * x[5,0:n] * x[6,0:n] )

  return value

def cyclic7_m ( ):

#*****************************************************************************80
#
## cyclic7_m() returns the number of variables in the cyclic7 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 7

  return m

def cyclic7_test ( ):

#*****************************************************************************80
#
## cyclic7_test() uses sampling to estimate the range of the CYCLIC7 polynomial.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 January 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'cyclic7_test():' )
  print ( '  Use N sample values of the Cyclic7 polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = cyclic7_m ( )
  l, u = cyclic7_b ( m )
  print ( '  cyclic7: [-5.0, +7.0]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = cyclic7_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def cyclic8_b ( m ):

#*****************************************************************************80
#
## cyclic8_b() returns the bounds in the cyclic8 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0 ] )
  u = np.array ( [ +1.0, +1.0, +1.0, +1.0, +1.0, +1.0, +1.0, +1.0 ] )

  return u, l

def cyclic8_f ( m, n, x ):

#*****************************************************************************80
#
## cyclic8_f() returns the function in the cyclic8 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
      x[0,0:n] * x[1,0:n] * x[2,0:n] * x[3,0:n] * x[4,0:n] * x[5,0:n] * x[6,0:n]            \
    + x[0,0:n] * x[1,0:n] * x[2,0:n] * x[3,0:n] * x[4,0:n] * x[5,0:n]            * x[7,0:n] \
    + x[0,0:n] * x[1,0:n] * x[2,0:n] * x[3,0:n] * x[4,0:n]            * x[6,0:n] * x[7,0:n] \
    + x[0,0:n] * x[1,0:n] * x[2,0:n] * x[3,0:n]            * x[5,0:n] * x[6,0:n] * x[7,0:n] \
    + x[0,0:n] * x[1,0:n] * x[2,0:n]            * x[4,0:n] * x[5,0:n] * x[6,0:n] * x[7,0:n] \
    + x[0,0:n] * x[1,0:n]            * x[3,0:n] * x[4,0:n] * x[5,0:n] * x[6,0:n] * x[7,0:n] \
    + x[0,0:n]            * x[2,0:n] * x[3,0:n] * x[4,0:n] * x[5,0:n] * x[6,0:n] * x[7,0:n] \
    +            x[1,0:n] * x[2,0:n] * x[3,0:n] * x[4,0:n] * x[5,0:n] * x[6,0:n] * x[7,0:n] )

  return value

def cyclic8_m ( ):

#*****************************************************************************80
#
## cyclic8_m() returns the number of variables in the cyclic8 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 8

  return m

def cyclic8_test ( ):

#*****************************************************************************80
#
## cyclic8_test() uses sampling to estimate the range of the CYCLIC8 polynomial.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 January 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'cyclic8_test():' )
  print ( '  Use N sample values of the Cyclic8 polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = cyclic8_m ( )
  l, u = cyclic8_b ( m )
  print ( '  cyclic8: [-8.0, +8.0]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = cyclic8_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def goldstein_price_b ( m ):

#*****************************************************************************80
#
## goldstein_price_b() returns the bounds in the goldstein_price problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -2.0, -2.0 ] )
  u = np.array ( [ +2.0, +2.0 ] )

  return l, u

def goldstein_price_f ( m, n, x ):

#*****************************************************************************80
#
## goldstein_price_f() returns the function in the goldstein_price problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  g = ( \
    1.0 + ( x[0,0:n] + x[1,0:n] + 1.0 ) ** 2 \
    * ( 19.0 - 14.0 * x[0,0:n] + 3.0 * x[0,0:n] **2 \
    - 14.0 * x[1,0:n] + 6.0 * x[0,0:n] * x[1,0:n] \
    + 3.0 * x[1,0:n] ** 2 ) )

  h = ( \
    30.0 + ( 2.0 * x[0,0:n] - 3.0 * x[1,0:n] ) ** 2 \
    * ( 18.0 - 32.0 * x[0,0:n] + 12.0 * x[0,0:n] ** 2 \
    + 48.0 * x[1,0:n] - 36.0 * x[0,0:n] * x[1,0:n] \
    + 27.0 * x[1,0:n] ** 2 ) )

  value = ( g * h )

  return value

def goldstein_price_m ( ):

#*****************************************************************************80
#
## goldstein_price_m() returns the number of variables in the goldstein_price problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 2

  return m

def goldstein_price_test ( ):

#*****************************************************************************80
#
## goldstein_price_test() uses sampling to estimate the range of the goldstein_price polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'goldstein_price_test():' )
  print ( '  Use N sample values of the Goldstein-Price polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = goldstein_price_m ( )
  l, u = goldstein_price_b ( m )
  print ( '  goldstein_price: [ 3, ? ]:' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = goldstein_price_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def hairer_b ( m ):

#*****************************************************************************80
#
## hairer_b() returns the bounds in the hairer problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ +2.0, +2.0, +2.0, -5.0, -5.0, -5.0 ] )
  u = np.array ( [ +5.0, +5.0, +5.0, -2.0, -2.0, -2.0 ] )

  return l, u

def hairer_f ( m, n, x ):

#*****************************************************************************80
#
## hairer_f() returns the function in the hairer problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
    +           x[2,0:n] ** 3 * x[3,0:n] \
    +           x[1,0:n] ** 3 * x[4,0:n] \
    +           x[0,0:n] ** 3 * x[5,0:n] \
    - 0.25 )

  return value

def hairer_m ( ):

#*****************************************************************************80
#
## hairer_m() returns the number of variables in the hairer problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 6

  return m

def hairer_test ( ):

#*****************************************************************************80
#
## hairer_test() uses sampling to estimate the range of the HAIRER polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hairer_test():' )
  print ( '  Use N sample values of the Hairer polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = hairer_m ( )
  l, u = hairer_b ( m )
  print ( '  hairer: [-1875.25, -48.25]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = hairer_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def heart_b ( m ):

#*****************************************************************************80
#
## heart_b() returns the bounds in the heart problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -0.1,  0.4, -0.7, -0.7, +0.1, -0.1, -0.3, -1.1 ] )
  u = np.array ( [  0.4, +1.0, -0.4, +0.4, +0.2, +0.2, +1.1, -0.3 ] )

  return l, u

def heart_f ( m, n, x ):

#*****************************************************************************80
#
## heart_f() returns the function in the heart problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real x[M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
    +       x[0,0:n] * x[5,0:n] ** 3                 \
    - 3.0 * x[0,0:n] * x[5,0:n]      * x[6,0:n] ** 2 \
    +       x[2,0:n] * x[6,0:n] ** 3                 \
    - 3.0 * x[2,0:n] * x[6,0:n]      * x[5,0:n] ** 2 \
    +       x[1,0:n] * x[4,0:n] ** 3                 \
    - 3.0 * x[1,0:n] * x[4,0:n]      * x[7,0:n] ** 2 \
    +       x[3,0:n] * x[7,0:n] ** 3                 \
    - 3.0 * x[3,0:n] * x[7,0:n]      * x[4,0:n] ** 2 \
    + 0.9563453 )
 
  return value

def heart_m ( ):

#*****************************************************************************80
#
## heart_m() returns the number of variables in the heart problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 8

  return m

def heart_test ( ):

#*****************************************************************************80
#
## heart_test() uses sampling to estimate the range of the HEART polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'heart_test():' )
  print ( '  Use N sample values of the Heart polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = heart_m ( )
  l, u = heart_b ( m )
  print ( '  heart: [-1.36775, +1.74345327935]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = heart_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def himmelblau_b ( m ):

#*****************************************************************************80
#
## himmelblau_b() returns the bounds in the himmelblau problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -5.0, -5.0 ] )
  u = np.array ( [ +5.0, +5.0 ] )

  return l, u

def himmelblau_f ( m, n, x ):

#*****************************************************************************80
#
## himmelblau_f() returns the function in the himmelblau problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  g = x[0,0:n] ** 2 + x[1,0:n]      - 11.0
  h = x[0,0:n]      + x[1,0:n] ** 2 -  7.0

  value = ( g ** 2 + h ** 2 )

  return value

def himmelblau_m ( ):

#*****************************************************************************80
#
## himmelblau_m() returns the number of variables in the himmelblau problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 2

  return m

def himmelblau_test ( ):

#*****************************************************************************80
#
## himmelblau_test() uses sampling to estimate the range of the HIMMELBLAU polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'himmelblau_test():' )
  print ( '  Use N sample values of the Himmelblau polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = himmelblau_m ( )
  l, u = himmelblau_b ( m )
  print ( '  himmelblau: [0, ?]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = himmelblau_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def hunecke_b ( m ):

#*****************************************************************************80
#
## hunecke_b() returns the bounds in the hunecke problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [  0.0, +2.0, -2.0, +1.0, -2.0 ] )
  u = np.array ( [ +1.0, +3.0, -1.0, +3.0, -1.0 ] )

  return l, u

def hunecke_f ( m, n, x ):

#*****************************************************************************80
#
## hunecke_f() returns the function in the hunecke problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
    +       x[1,0:n] ** 6  * x[2,0:n]                                                 \
    +       x[1,0:n]       * x[2,0:n] ** 6                                            \
    +       x[0,0:n] ** 2  * x[1,0:n] ** 4 * x[4,0:n]                                 \
    - 3.0 * x[0,0:n]       * x[1,0:n] ** 2 * x[2,0:n] ** 2 * x[3,0:n]      * x[4,0:n] \
    +       x[2,0:n] ** 4  * x[3,0:n] ** 2 * x[4,0:n]                                 \
    -       x[0,0:n] ** 3  * x[2,0:n]      * x[3,0:n]      * x[4,0:n] ** 2            \
    -       x[0,0:n]       * x[1,0:n]      * x[3,0:n] ** 3 * x[4,0:n] ** 2            \
    +       x[1,0:n]       * x[2,0:n]      * x[4,0:n] ** 5 )

  return value

def hunecke_m ( ):

#*****************************************************************************80
#
## hunecke_m() returns the number of variables in the hunecke problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 5

  return m

def hunecke_test ( ):

#*****************************************************************************80
#
## hunecke_test() uses sampling to estimate the range of the HUNECKE polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hunecke_test():' )
  print ( '  Use N sample values of the Hunecke polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = hunecke_m ( )
  l, u = hunecke_b ( m )
  print ( '  hunecke: [-1436.515078155, +161.120543283]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = hunecke_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def kearfott_b ( m ):

#*****************************************************************************80
#
## kearfott_b() returns the bounds in the kearfott problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = -2.0 * np.ones ( m )
  u = +2.0 * np.ones ( m )

  return l, u

def kearfott_f ( m, n, x ):

#*****************************************************************************80
#
## kearfott_f() returns the function in the kearfott problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  import numpy as np

  value = np.zeros ( n )

  for i in range ( 0, m - 1 ):
    value = value \
      + ( x[i,0:n] ** 2   - x[i+1,0:n] ) ** 2 \
      + ( x[m-1,0:n] ** 2 - x[i,0:n]   ) ** 2

  return value

def kearfott_m ( ):

#*****************************************************************************80
#
## kearfott_m() returns the number of variables in the kearfott problem.
#
#  Discussion
#
#    Actually, the function can be defined for any 2 <= M.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 4

  return m

def kearfott_test ( ):

#*****************************************************************************80
#
## kearfott_test() uses sampling to estimate the range of the KEARFOTT polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'kearfott_test():' )
  print ( '  Use N sample values of the Kearfott polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = kearfott_m ( )
  l, u = kearfott_b ( m )
  print ( '  kearfott: [ 0, ? ]:' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = kearfott_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def lv3_b ( m ):

#*****************************************************************************80
#
## lv3_b() returns the bounds in the lv3 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -1.5, -1.5, -1.5 ] )
  u = np.array ( [ +2.0, +2.0, +2.0 ] )

  return l, u

def lv3_f ( m, n, x ):

#*****************************************************************************80
#
## lv3_f() returns the function in the lv3 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
    -       x[0,0:n] * x[1,0:n] ** 2 \
    +       x[0,0:n] * x[2,0:n] ** 2 \
    - 1.1 * x[0,0:n] \
    + 1.0 )
 
  return value

def lv3_m ( ):

#*****************************************************************************80
#
## lv3_m() returns the number of variables in the lv3 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 3

  return m

def lv3_test ( ):

#*****************************************************************************80
#
## lv3_test() uses sampling to estimate the range of the LV3 polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'lv3_test():' )
  print ( '  Use N sample values of the LV3 polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = lv3_m ( )
  l, u = lv3_b ( m )
  print ( '  lv3: [-9.35, +14.8 ]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = lv3_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def lv4_b ( m ):

#*****************************************************************************80
#
## lv4_b() returns the bounds in the lv4 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -2.0, -2.0, -2.0, -2.0 ] )
  u = np.array ( [ +2.0, +2.0, +2.0, +2.0 ] )

  return l, u

def lv4_f ( m, n, x ):

#*****************************************************************************80
#
## lv4_f() returns the function in the lv4 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
    -       x[0,0:n] * x[1,0:n] ** 2 \
    +       x[0,0:n] * x[2,0:n] ** 2 \
    +       x[0,0:n] * x[3,0:n] ** 2 \
    - 1.1 * x[0,0:n] \
    + 1.0 )
 
  return value

def lv4_m ( ):

#*****************************************************************************80
#
## lv4_m() returns the number of variables in the lv4 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 4

  return m

def lv4_test ( ):

#*****************************************************************************80
#
## lv4_test() uses sampling to estimate the range of the LV4 polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'lv4_test():' )
  print ( '  Use N sample values of the LV4 polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = lv4_m ( )
  l, u = lv4_b ( m )
  print ( '  lv4: [-20.8, +22.8]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = lv4_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def magnetism6_b ( m ):

#*****************************************************************************80
#
## magnetism6_b() returns the bounds in the magnetism6 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0 ] )
  u = np.array ( [ +5.0, +5.0, +5.0, +5.0, +5.0, +5.0, +5.0 ] )

  return l, u

def magnetism6_f ( m, n, x ):

#*****************************************************************************80
#
## magnetism6_f() returns the function in the magnetism6 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
      2.0 * x[0,0:n] ** 2 \
    + 2.0 * x[1,0:n] ** 2 \
    + 2.0 * x[2,0:n] ** 2 \
    + 2.0 * x[3,0:n] ** 2 \
    + 2.0 * x[4,0:n] ** 2 \
    +       x[5,0:n] ** 2 \
    -       x[5,0:n] )
 
  return value

def magnetism6_m ( ):

#*****************************************************************************80
#
## magnetism6_m() returns the number of variables in the magnetism6 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 6

  return m

def magnetism6_test ( ):

#*****************************************************************************80
#
## magnetism6_test() uses sampling to estimate the range of the MAGNETISM6 polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'magnetism6_test():' )
  print ( '  Use N sample values of the Magnetism6 polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = magnetism6_m ( )
  l, u = magnetism6_b ( m )
  print ( '  magnetism6: [-0.25, +280.0]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = magnetism6_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def magnetism7_b ( m ):

#*****************************************************************************80
#
## magnetism7_b() returns the bounds in the magnetism7 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0 ] )
  u = np.array ( [ +1.0, +1.0, +1.0, +1.0, +1.0, +1.0, +1.0 ] )

  return l, u

def magnetism7_f ( m, n, x ):

#*****************************************************************************80
#
## magnetism7_f() returns the function in the magnetism7 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
            x[0,0:n] ** 2 \
    + 2.0 * x[1,0:n] ** 2 \
    + 2.0 * x[2,0:n] ** 2 \
    + 2.0 * x[3,0:n] ** 2 \
    + 2.0 * x[4,0:n] ** 2 \
    + 2.0 * x[5,0:n] ** 2 \
    + 2.0 * x[6,0:n] ** 2 \
    -       x[0,0:n] )
 
  return value

def magnetism7_m ( ):

#*****************************************************************************80
#
## magnetism7_m() returns the number of variables in the magnetism7 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 7

  return m

def magnetism7_test ( ):

#*****************************************************************************80
#
## magnetism7_test() uses sampling to estimate the range of the MAGNETISM7 polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'magnetism7_test():' )
  print ( '  Use N sample values of the Magnetism7 polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = magnetism7_m ( )
  l, u = magnetism7_b ( m )
  print ( '  magnetism7: [-0.25, +330.0]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = magnetism7_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def polynomials_test ( ):

#*****************************************************************************80
#
## polynomials_test() tests polynomials().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'polynomials_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test polynomials().' )

  butcher_test ( )
  camel_test ( )
  camera_test ( )
  caprasse_test ( )
  cyclic5_test ( )
  cyclic7_test ( )
  cyclic8_test ( )
  goldstein_price_test ( )
  hairer_test ( )
  heart_test ( )
  himmelblau_test ( )
  hunecke_test ( )
  kearfott_test ( )
  lv3_test ( )
  lv4_test ( )
  magnetism6_test ( )
  magnetism7_test ( )
  quadratic_test ( )
  rd_test ( )
  reimer5_test ( )
  reimer6_test ( )
  rosenbrock_test ( )
  schwefel_test ( )
  smith1_test ( )
  smith2_test ( )
  virasoro_test ( )
  wright_test ( )
  zakharov_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'polynomials_test():' )
  print ( '  Normal end of execution.' )
  return

def quadratic_b ( m ):

#*****************************************************************************80
#
## quadratic_b() returns the bounds in the quadratic problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    real L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l =  -99.99 * np.ones ( m )
  u = +100.00 * np.ones ( m )

  return l, u

def quadratic_f ( m, n, x ):

#*****************************************************************************80
#
## quadratic_f() returns the function in the quadratic problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    real VALUE(N), the value of the function at X.
#
  import numpy as np

  r = - 2.0

  value = - r * np.ones ( n )

  for i in range ( 0, m ):
    value = value + x[i,0:n] ** 2

  return value

def quadratic_m ( ):

#*****************************************************************************80
#
## quadratic_m() returns the number of variables in the quadratic problem.
#
#  Discussion
#
#    Actually, the function can be defined for any 1 <= M.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 8

  return m

def quadratic_test ( ):

#*****************************************************************************80
#
## quadratic_test() uses sampling to estimate the range of the QUADRATIC polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'quadratic_test():' )
  print ( '  Use N sample values of the Quadratic polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = quadratic_m ( )
  l, u = quadratic_b ( m )
  print ( '  quadratic: [ -2, ? ]:' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = quadratic_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print() prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some() prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_uniform_abvec ( m, n, a, b ):

#*****************************************************************************80
#
## r8mat_uniform_abvec() returns a pseudorandom R8MAT with row ranges.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the array.
#
#    real A(M), B(M), the range for each row.
#
#  Output:
#
#    real R(M,N), an array of random values.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  r = rng.random ( size = [ m, n ] )

  for i in range ( 0, m ):
    r[i,0:n] = a[i] + ( b[i] - a[i] ) * r[i,0:n]

  return r

def r8mat_uniform_abvec_test ( ):

#*****************************************************************************80
#
## r8mat_uniform_abvec_test() tests r8mat_uniform_abvec().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 December 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4
  a = np.array ( [  2.0, 0.0, -1.0, 100.0, 0.1 ] )
  b = np.array ( [ 10.0, 1.0,  0.0, 110.0, 0.2 ] )

  print ( '' )
  print ( 'r8mat_uniform_abvec_test():' )
  print ( '  r8mat_uniform_abvec() computes a random R8MAT.' )
  print ( '' )

  r8vec2_print ( a, b, '  Lower and upper row limits:' )

  v = r8mat_uniform_abvec ( m, n, a, b )

  r8mat_print ( m, n, v, '  Random R8MAT:' )

  return

def r8vec2_print ( a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  n = len ( a1 )

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## r8vec2_print_test() tests r8vec2_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec2_print_test():' )
  print ( '  r8vec2_print() prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( v, w, '  Print a pair of R8VEC\'s:' )

  return

def rd_b ( m ):

#*****************************************************************************80
#
## rd_b() returns the bounds in the rd problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -5.0, -5.0, -5.0 ] )
  u = np.array ( [ +5.0, +5.0, +5.0 ] )

  return l, u 

def rd_f ( m, n, x ):

#*****************************************************************************80
#
## rd_f() returns the function in the rd problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
    -               x[0,0:n] \
    + 2.0         * x[1,0:n] \
    -               x[2,0:n] \
    - 0.835634534 * x[1,0:n] \
    - 0.835634534 * x[1,0:n] ** 2 )

  return value

def rd_m ( ):

#*****************************************************************************80
#
## rd_m() returns the number of variables in the rd problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 3

  return m

def rd_test ( ):

#*****************************************************************************80
#
## rd_test() uses sampling to estimate the range of the RD polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'rd_test():' )
  print ( '  Use N sample values of the RD polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = rd_m ( )
  l, u = rd_b ( m )
  print ( '  rd: [-36.71269068, +10.40560403]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = rd_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def reimer5_b ( m ):

#*****************************************************************************80
#
## reimer5_b() returns the bounds in the reimer5 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -1.0, -1.0, -1.0, -1.0, -1.0 ] )
  u = np.array ( [ +1.0, +1.0, +1.0, +1.0, +1.0 ] )

  return l, u

def reimer5_f ( m, n, x ):

#*****************************************************************************80
#
## reimer5_f() returns the function in the reimer5 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
    - 1.0 \
    + 2.0 * x[0,0:n] ** 6 \
    - 2.0 * x[1,0:n] ** 6 \
    + 2.0 * x[2,0:n] ** 6 \
    - 2.0 * x[3,0:n] ** 6 \
    + 2.0 * x[4,0:n] ** 6 )

  return value

def reimer5_m ( ):

#*****************************************************************************80
#
## reimer5_m() returns the number of variables in the reimer5 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 5

  return m

def reimer5_test ( ):

#*****************************************************************************80
#
## reimer5_test() uses sampling to estimate the range of the REIMER5 polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'reimer5_test():' )
  print ( '  Use N sample values of the Reimer5 polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = reimer5_m ( )
  l, u = reimer5_b ( m )
  print ( '  reimer5: [-5.0, +5.0]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = reimer5_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def reimer6_b ( m ):

#*****************************************************************************80
#
## reimer6_b() returns the bounds in the reimer6 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -5.0, -5.0, -5.0, -5.0, -5.0, -5.0 ] )
  u = np.array ( [ +5.0, +5.0, +5.0, +5.0, +5.0, +5.0 ] )

  return l, u

def reimer6_f ( m, n, x ):

#*****************************************************************************80
#
## reimer6_f() returns the function in the reimer6 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
    - 1.0 \
    + 2.0 * x[0,0:n] ** 7 \
    - 2.0 * x[1,0:n] ** 7 \
    + 2.0 * x[2,0:n] ** 7 \
    - 2.0 * x[3,0:n] ** 7 \
    + 2.0 * x[4,0:n] ** 7 \
    - 2.0 * x[5,0:n] ** 7 )

  return value

def reimer6_m ( ):

#*****************************************************************************80
#
## reimer6_m() returns the number of variables in the reimer6 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 6

  return m

def reimer6_test ( ):

#*****************************************************************************80
#
## reimer6_test() uses sampling to estimate the range of the REIMER6 polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'reimer6_test():' )
  print ( '  Use N sample values of the Reimer6 polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = reimer6_m ( )
  l, u = reimer6_b ( m )
  print ( '  reimer6: [-937501, +937499]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = reimer6_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def rosenbrock_b ( m ):

#*****************************************************************************80
#
## rosenbrock_b() returns the bounds in the rosenbrock problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l =  -5.0 * np.ones ( m )
  u = +10.0 * np.ones ( m )

  return l, u

def rosenbrock_f ( m, n, x ):

#*****************************************************************************80
#
## rosenbrock_f() returns the function in the rosenbrock problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  import numpy as np

  value = np.zeros ( n )

  for i in range ( 0, m - 1 ):
    value = value \
      + 100.0 * ( x[i,0:n] - x[i+1,0:n] ) ** 2 \
      +         ( x[i,0:n] - 1.0    ) ** 2

  return value

def rosenbrock_m ( ):

#*****************************************************************************80
#
## rosenbrock_m() returns the number of variables in the rosenbrock problem.
#
#  Discussion
#
#    Actually, the function can be defined for any 2 <= M.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 4

  return m

def rosenbrock_test ( ):

#*****************************************************************************80
#
## rosenbrock_test() uses sampling to estimate the range of the ROSENBROCK polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'rosenbrock_test():' )
  print ( '  Use N sample values of the Rosenbrock polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = rosenbrock_m ( )
  l, u = rosenbrock_b ( m )
  print ( '  rosenbrock: [ 0, ? ]:' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = rosenbrock_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def schwefel_b ( m ):

#*****************************************************************************80
#
## schwefel_b() returns the bounds in the schwefel problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -10.0, -10.0, -10.0 ] )
  u = np.array ( [ +10.0, +10.0, +10.0 ] )

  return l, u

def schwefel_f ( m, n, x ):

#*****************************************************************************80
#
## schwefel_f() returns the function in the schwefel problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
      ( x[0,1:n] - x[1,1:n] ** 2 ) ** 2 \
    + ( x[1,1:n] - 1.0           ) ** 2 \
    + ( x[0,1:n] - x[2,1:n] ** 2 ) ** 2 \
    + ( x[2,1:n] - 1.0           ) ** 2 )

  return value

def schwefel_m ( ):

#*****************************************************************************80
#
## schwefel_m() returns the number of variables in the schwefel problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 3

  return m

def schwefel_test ( ):

#*****************************************************************************80
#
## schwefel_test() uses sampling to estimate the range of the SCHWEFEL polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'schwefel_test():' )
  print ( '  Use N sample values of the Schwefel polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = schwefel_m ( )
  l, u = schwefel_b ( m )
  print ( '  schwefel: [ 0, ? ]:' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = schwefel_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def smith1_b ( m ):

#*****************************************************************************80
#
## smith1_b() returns the bounds in the smith1 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#  Reference:
#
#    Andrew Smith,
#    Fast construction of constant bound functions for sparse polynomials,
#    Journal of Global Optimization,
#    Volume 43, 2009, pages 445-458.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ +1.0, +2.0, +4.0, -5.0,  +2.0 ] )
  u = np.array ( [ +2.0, +3.0, +6.0, -2.0, +10.0 ] )

  return l, u

def smith1_f ( m, n, x ):

#*****************************************************************************80
#
## smith1_f() returns the function in the smith1 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Andrew Smith,
#    Fast construction of constant bound functions for sparse polynomials,
#    Journal of Global Optimization,
#    Volume 43, 2009, pages 445-458.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
      3.0 * x[0,0:n] ** 2 * x[1,0:n] ** 3 * x[2,0:n] ** 4 \
    +       x[0,0:n] ** 3 * x[1,0:n]      * x[2,0:n] ** 3 \
    - 5.0 * x[0,0:n]      * x[1,0:n]      * x[3,0:n] ** 5 \
    +       x[2,0:n]      * x[3,0:n]      * x[4,0:n] ** 3 )
 
  return value

def smith1_m ( ):

#*****************************************************************************80
#
## smith1_m() returns the number of variables in the smith1 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Andrew Smith,
#    Fast construction of constant bound functions for sparse polynomials,
#    Journal of Global Optimization,
#    Volume 43, 2009, pages 445-458.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 5

  return m

def smith1_test ( ):

#*****************************************************************************80
#
## smith1_test() uses sampling to estimate the range of the SMITH1 polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'smith1_test():' )
  print ( '  Use N sample values of the Smith1 polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = smith1_m ( )
  l, u = smith1_b ( m )
  print ( '  smith1: [ ?, ? ]:' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = smith1_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def smith2_b ( m ):

#*****************************************************************************80
#
## smith2_b() returns the bounds in the smith2 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#  Reference:
#
#    Andrew Smith,
#    Fast construction of constant bound functions for sparse polynomials,
#    Journal of Global Optimization,
#    Volume 43, 2009, pages 445-458.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ +1.0, +1.0, +1.0, +1.0, +1.0, +1.0, +1.0 ] )
  u = np.array ( [ +2.0, +2.0, +2.0, +2.0, +2.0, +2.0, +2.0 ] )

  return l, u

def smith2_f ( m, n, x ):

#*****************************************************************************80
#
## smith2_f() returns the function in the smith2 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Andrew Smith,
#    Fast construction of constant bound functions for sparse polynomials,
#    Journal of Global Optimization,
#    Volume 43, 2009, pages 445-458.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real x[M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
       3.0  * x[0,0:n]      * x[1,0:n] ** 5                 \
    +  2.0  * x[0,0:n] ** 4 * x[1,0:n]                      \
    -  8.0  * x[0,0:n] ** 2 * x[2,0:n] ** 6 * x[3,0:n] ** 2 \
    -         x[0,0:n]      * x[3,0:n] ** 8                 \
    +  3.0  * x[1,0:n] ** 3 * x[4,0:n]                      \
    - 10.0  * x[3,0:n] ** 5 * x[4,0:n] ** 5 * x[5,0:n] ** 5 \
    -  0.01 * x[4,0:n] ** 2 * x[5,0:n] ** 2                 \
    +  4.0  * x[4,0:n] ** 3 * x[6,0:n] ** 4 )
 
  return value

def smith2_m ( ):

#*****************************************************************************80
#
## smith2_m() returns the number of variables in the smith2 problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Andrew Smith,
#    Fast construction of constant bound functions for sparse polynomials,
#    Journal of Global Optimization,
#    Volume 43, 2009, pages 445-458.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 7

  return m

def smith2_test ( ):

#*****************************************************************************80
#
## smith2_test() uses sampling to estimate the range of the SMITH2 polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'smith2_test():' )
  print ( '  Use N sample values of the Smith2 polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = smith2_m ( )
  l, u = smith2_b ( m )
  print ( '  smith2: [ ?, ? ]:' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = smith2_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def virasoro_b ( m ):

#*****************************************************************************80
#
## virasoro_b() returns the bounds in the virasoro problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0 ] )
  u = np.array ( [ +1.0, +1.0, +1.0, +1.0, +1.0, +1.0, +1.0, +1.0 ] )

  return l, u

def virasoro_f ( m, n, x ):

#*****************************************************************************80
#
## virasoro_f() returns the function in the virasoro problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real x[M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
    - 2.0 * x[0,0:n]      * x[3,0:n] \
    + 2.0 * x[0,0:n]      * x[6,0:n] \
    - 2.0 * x[1,0:n]      * x[4,0:n] \
    + 2.0 * x[1,0:n]      * x[6,0:n] \
    - 2.0 * x[2,0:n]      * x[5,0:n] \
    + 2.0 * x[2,0:n]      * x[6,0:n] \
    + 2.0 * x[3,0:n]      * x[6,0:n] \
    + 2.0 * x[4,0:n]      * x[6,0:n] \
    + 8.0 * x[5,0:n]      * x[6,0:n] \
    - 6.0 * x[5,0:n]      * x[7,0:n] \
    + 8.0 * x[6,0:n] ** 2             \
    + 6.0 * x[6,0:n]      * x[7,0:n] \
    -       x[6,0:n] )

  return value

def virasoro_m ( ):

#*****************************************************************************80
#
## virasoro_m() returns the number of variables in the virasoro problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 8

  return m

def virasoro_test ( ):

#*****************************************************************************80
#
## virasoro_test() uses sampling to estimate the range of the VIRASORO polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'virasoro_test():' )
  print ( '  Use N sample values of the Virasoro polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = virasoro_m ( )
  l, u = virasoro_b ( m )
  print ( '  virasoro: [-29.0, +21.0]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = virasoro_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def wright_b ( m ):

#*****************************************************************************80
#
## wright_b() returns the bounds in the wright problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -0.5, -0.5, -0.5, -0.5, -0.5 ] )
  u = np.array ( [ +0.5, +0.5, +0.5, +0.5, +0.5 ] )

  return l, u

def wright_f ( m, n, x ):

#*****************************************************************************80
#
## wright_f() returns the function in the wright problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real x[M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  value = ( \
      x[4,0:n] ** 2 \
    + x[0,0:n] \
    + x[1,0:n] \
    + x[2,0:n] \
    + x[3,0:n] \
    - x[4,0:n] \
    - 10.0 )

  return value

def wright_m ( ):

#*****************************************************************************80
#
## wright_m() returns the number of variables in the wright problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 5

  return m

def wright_test ( ):

#*****************************************************************************80
#
## wright_test() uses sampling to estimate the range of the WRIGHT polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'wright_test():' )
  print ( '  Use N sample values of the Wright polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = wright_m ( )
  l, u = wright_b ( m )
  print ( '  wright: [-30.25, 40.0 ]' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = wright_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

def zakharov_b ( m ):

#*****************************************************************************80
#
## zakharov_b() returns the bounds in the zakharov problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#  Output:
#
#    integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l =  -5.0 * np.ones ( m )
  u = +10.0 * np.ones ( m )

  return l, u

def zakharov_f ( m, n, x ):

#*****************************************************************************80
#
## zakharov_f() returns the function in the zakharov problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Input:
#
#    integer M, the number of variables.
#
#    integer N, the number of points.
#
#    real X(M,N), the points.
#
#  Output:
#
#    integer VALUE(N), the value of the function at X.
#
  import numpy as np

  s1 = np.zeros ( n )
  s2 = np.zeros ( n )

  for i in range ( 0, m ):
    s1 = s1 +                         x[i,0:n] ** 2
    s2 = s2 + 0.5 * float ( i + 1 ) * x[i,0:n]

  value = s1 + s2 ** 2 + s2 ** 4

  return value

def zakharov_m ( ):

#*****************************************************************************80
#
## zakharov_m() returns the number of variables in the zakharov problem.
#
#  Discussion
#
#    Actually, the function can be defined for any 1 <= M.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Output:
#
#    integer M, the number of variables.
#
  m = 5

  return m

def zakharov_test ( ):

#*****************************************************************************80
#
## zakharov_test() uses sampling to estimate the range of the ZAKHAROV polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'zakharov_test():' )
  print ( '  Use N sample values of the Zakharov polynomial to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = zakharov_m ( )
  l, u = zakharov_b ( m )
  print ( '  zakharov: [ 0, ? ]:' )

  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x = r8mat_uniform_abvec ( m, n, u, l )
    f = zakharov_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  polynomials_test ( )
  timestamp ( )

