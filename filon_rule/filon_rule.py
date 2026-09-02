#! /usr/bin/env python3
#
def filon_rule_test ( ):

#*****************************************************************************80
#
## filon_rule_test() tests filon_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'filon_rule_test():' )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  Test filon_rule():' )

  filon_test01 ( )
  filon_test02 ( )
  filon_test03 ( )
  filon_test04 ( )
  filon_test05 ( )
  filon_test06 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'filon_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def filon_fun_cos ( n, f, a, b, t ):

#*****************************************************************************80
#
## filon_fun_cos() uses Filon's method on integrals with a cosine factor.
#
#  Discussion:
#
#    The integral to be approximated has the form:
#
#      Integral ( A <= X <= B ) F(X) * COS(T*X) dX
#
#    where T is user specified.
#
#    The function is interpolated over each subinterval by
#    a parabolic arc.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Chase, Lloyd Fosdick,
#    An Algorithm for Filon Quadrature,
#    Communications of the Association for Computing Machinery,
#    Volume 12, Number 8, August 1969, pages 453-457.
#
#    Stephen Chase, Lloyd Fosdick,
#    Algorithm 353:
#    Filon Quadrature,
#    Communications of the Association for Computing Machinery,
#    Volume 12, Number 8, August 1969, pages 457-458.
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    integer N, the number of data points.
#    N must be odd, and greater than 1.
#
#    function pointer F, the subroutine which evaluates the integrand,
#    of the form "function fx = f ( n, x )".
#
#    real A, B, the limits of integration.
#
#    real T, the multiplier of the X argument of the cosine.
#
#  Output:
#
#    real VALUE, the approximate value of the integral.
#
  import numpy as np

  if ( a == b ):
    value = 0.0
    return value
 
  if ( n <= 1 ):
    print ( '' )
    print ( 'filon_fun_cos(): Fatal error!' )
    print ( '  N < 2' )
    print ( '  N = ', n )
    raise Exception ( 'filon_fun_cos(): Fatal error!' )
 
  if ( ( n % 2 ) != 1 ):
    print ( '' )
    print ( 'filon_fun_cos(): Fatal error!' )
    print ( '  N must be odd.' )
    print ( '  N = ', n )
    raise Exception ( 'filon_fun_cos(): Fatal error!' )
#
#  Set the X values.
#
  x = np.linspace ( a, b, n )
  h = ( b - a ) / ( n - 1 )

  theta = t * h
  sint = np.sin ( theta )
  cost = np.cos ( theta )

  if ( 6.0 * np.abs ( theta ) <= 1.0 ):

    alpha = 2.0 * theta**3 /   45.0 \
          - 2.0 * theta**5 /  315.0 \
          + 2.0 * theta**7 / 4725.0
  
    beta =  2.0            /     3.0 \
          + 2.0 * theta**2 /    15.0 \
          - 4.0 * theta**4 /   105.0 \
          + 2.0 * theta**6 /   567.0 \
          - 4.0 * theta**8 / 22275.0

    gamma = 4.0            /      3.0 \
          - 2.0 * theta**2 /     15.0 \
          +       theta**4 /    210.0 \
          -       theta**6 /  11340.0

  else:

    alpha = ( theta**2 + theta * sint * cost - 2.0 * sint**2 ) / theta**3

    beta = ( 2.0 * theta + 2.0 * theta * cost**2 \
      - 4.0 * sint * cost ) / theta**3

    gamma = 4.0 * ( sint - theta * cost ) / theta**3
#
#  Tabulate the function.
#
  ftab = f ( n, x )

  c2n = np.sum ( ftab[0:n:2] * np.cos ( t * x[0:n:2] ) ) \
    - 0.5 * ( ftab[n-1] * np.cos ( t * x[n-1] ) \
            + ftab[0] * np.cos ( t * x[0] ) )

  c2nm1 = np.sum ( ftab[1:n-1:2] * np.cos ( t * x[1:n-1:2] ) )
 
  value = h * ( \
      alpha * ( ftab[n-1] * np.sin ( t * x[n-1] ) \
              - ftab[0] * np.sin ( t * x[0] ) ) \
    + beta * c2n \
    + gamma * c2nm1 )

  return value

def filon_fun_sin ( n, f, a, b, t ):

#*****************************************************************************80
#
## filon_fun_sin() uses Filon's method on integrals with a sine factor.
#
#  Discussion:
#
#    The integral to be approximated has the form
#
#      Integral ( A <= X <= B ) F(X) * SIN(T*X) dX
#
#    where T is user specified.
#
#    The function is interpolated over each subinterval by
#    a parabolic arc.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Chase, Lloyd Fosdick,
#    An Algorithm for Filon Quadrature,
#    Communications of the Association for Computing Machinery,
#    Volume 12, Number 8, August 1969, pages 453-457.
#
#    Stephen Chase, Lloyd Fosdick,
#    Algorithm 353:
#    Filon Quadrature,
#    Communications of the Association for Computing Machinery,
#    Volume 12, Number 8, August 1969, pages 457-458.
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    integer N, the number of data points, 
#    including the endpoints.  N must be odd, and greater than 1.
#
#    function pointer F, the subroutine which evaluates the integrand,
#    of the form "function fx = f ( n, x )".
#
#    real A, B, the limits of integration.
#
#    real T, multiplier of the X argument of the sine.
#
#  Output:
#
#    real VALUE, the approximate value of the integral.
#
  import numpy as np

  if ( a == b ):
    value = 0.0
    return value
 
  if ( n <= 1 ):
    print ( '' )
    print ( 'filon_fun_sin(): Fatal error!' )
    print ( '  N < 2' )
    print ( '  N = ', n )
    raise Exception ( 'filon_fun_sin(): Fatal error!' )
 
  if ( ( n % 2 ) != 1 ):
    print ( '' )
    print ( 'filon_fun_sin(): Fatal error!' )
    print ( '  N must be odd.' )
    print ( '  N = ', n )
    raise Exception ( 'filon_fun_sin(): Fatal error!' )
#
#  Set the X values.
#
  x = np.linspace ( a, b, n )
  h = ( b - a ) / ( n - 1 )
  theta = t * h

  sint = np.sin ( theta )
  cost = np.cos ( theta )

  if ( 6.0 * np.abs ( theta ) <= 1.0 ):

    alpha = 2.0 * theta**3 /   45.0 \
          - 2.0 * theta**5 /  315.0 \
          + 2.0 * theta**7 / 4725.0
  
    beta =  2.0           /     3.0 \
          + 2.0 * theta**2 /    15.0 \
          - 4.0 * theta**4 /   105.0 \
          + 2.0 * theta**6 /   567.0 \
          - 4.0 * theta**8 / 22275.0

    gamma = 4.0           /      3.0 \
          - 2.0 * theta**2 /     15.0 \
          +       theta**4 /    210.0 \
          -       theta**6 /  11340.0

  else:
 
    alpha = ( theta**2 + theta * sint * cost \
      - 2.0 * sint**2 ) / theta**3

    beta = ( 2.0 * theta + 2.0 * theta * cost**2 \
      - 4.0 * sint * cost ) / theta**3

    gamma = 4.0 * ( sint - theta * cost ) / theta**3
#
#  Tabulate the function.
#
  ftab = f ( n, x )

  s2n = np.sum ( ftab[0:n:2] * np.sin ( t * x[0:n:2] ) ) \
    - 0.5 * ( ftab[n-1] * np.sin ( t * x[n-1] ) \
            + ftab[0] * np.sin ( t * x[0] ) )

  s2nm1 = np.sum ( ftab[1:n-1:2] * np.sin ( t * x[1:n-1:2] ) )

  value = h * ( \
      alpha * ( ftab[0] * np.cos ( t * x[0] ) \
              - ftab[n-1] * np.cos ( t * x[n-1] ) ) \
    + beta * s2n \
    + gamma * s2nm1 )
 
  return value

def filon_tab_cos ( n, ftab, a, b, t ):

#*****************************************************************************80
#
## filon_tab_cos() uses Filon's method on integrals with a cosine factor.
#
#  Discussion:
#
#    The integral to be approximated has the form:
#
#      Integral ( A <= X <= B ) F(X) * COS(T*X) dX
#
#    where T is user specified.
#
#    The function is interpolated over each subinterval by
#    a parabolic arc.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Chase, Lloyd Fosdick,
#    An Algorithm for Filon Quadrature,
#    Communications of the Association for Computing Machinery,
#    Volume 12, Number 8, August 1969, pages 453-457.
#
#    Stephen Chase, Lloyd Fosdick,
#    Algorithm 353:
#    Filon Quadrature,
#    Communications of the Association for Computing Machinery,
#    Volume 12, Number 8, August 1969, pages 457-458.
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    integer N, the number of data points.
#    N must be odd, and greater than 1.
#
#    real FTAB[n-1], contains the value of the function
#    at A, A+H, A+2*H, \ , B-H, B, where H = (B-A)/(N-1).
#
#    real A, B, the limits of integration.
#
#    real T, the multiplier of the X argument of the cosine.
#
#  Output:
#
#    real VALUE, the approximate value of the integral.
#
  import numpy as np

  if ( a == b ):
    value = 0.0
    return value
 
  if ( n <= 1 ):
    print ( '' )
    print ( 'filon_tab_cos(): Fatal error!' )
    print ( '  N < 2' )
    print ( '  N = ', n )
    raise Exception ( 'filon_tab_cos(): Fatal error!' )
 
  if ( ( n % 2 ) != 1 ):
    print ( '' )
    print ( 'filon_tab_cos(): Fatal error!' )
    print ( '  N must be odd.' )
    print ( '  N = ', n )
    raise Exception ( 'filon_tab_cos(): Fatal error!' )
#
#  Set the X values.
#
  x = np.linspace ( a, b, n )
  h = ( b - a ) / ( n - 1 )

  theta = t * h
  sint = np.sin ( theta )
  cost = np.cos ( theta )

  if ( 6.0 * np.abs ( theta ) <= 1.0 ):

    alpha = 2.0 * theta**3 /   45.0 \
          - 2.0 * theta**5 /  315.0 \
          + 2.0 * theta**7 / 4725.0
  
    beta =  2.0           /     3.0 \
          + 2.0 * theta**2 /    15.0 \
          - 4.0 * theta**4 /   105.0 \
          + 2.0 * theta**6 /   567.0 \
          - 4.0 * theta**8 / 22275.0

    gamma = 4.0           /      3.0 \
          - 2.0 * theta**2 /     15.0 \
          +       theta**4 /    210.0 \
          -       theta**6 /  11340.0

  else:

    alpha = ( theta**2 + theta * sint * cost - 2.0 * sint**2 ) / theta**3

    beta = ( 2.0 * theta + 2.0 * theta * cost**2 \
      - 4.0 * sint * cost ) / theta**3

    gamma = 4.0 * ( sint - theta * cost ) / theta**3

  c2n = np.sum ( ftab[0:n:2] * np.cos ( t * x[0:n:2] ) ) \
    - 0.5 * ( ftab[n-1] * np.cos ( t * x[n-1] ) \
            + ftab[0] * np.cos ( t * x[0] ) )

  c2nm1 = np.sum ( ftab[1:n-1:2] * np.cos ( t * x[1:n-1:2] ) )
 
  value = h * ( \
      alpha * ( ftab[n-1] * np.sin ( t * x[n-1] ) \
              - ftab[0] * np.sin ( t * x[0] ) ) \
    + beta * c2n \
    + gamma * c2nm1 )

  return value

def filon_tab_sin ( n, ftab, a, b, t ):

#*****************************************************************************80
#
## filon_tab_sin() uses Filon's method on integrals with a sine factor.
#
#  Discussion:
#
#    The integral to be approximated has the form
#
#      Integral ( A <= X <= B ) F(X) * SIN(T*X) dX
#
#    where T is user specified.
#
#    The function is interpolated over each subinterval by
#    a parabolic arc.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Chase, Lloyd Fosdick,
#    An Algorithm for Filon Quadrature,
#    Communications of the Association for Computing Machinery,
#    Volume 12, Number 8, August 1969, pages 453-457.
#
#    Stephen Chase, Lloyd Fosdick,
#    Algorithm 353:
#    Filon Quadrature,
#    Communications of the Association for Computing Machinery,
#    Volume 12, Number 8, August 1969, pages 457-458.
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    integer N, the number of data points, 
#    including the endpoints.  N must be odd, and greater than 1.
#
#    real FTAB[n-1], contains the value of the function
#    at A, A+H, A+2*H, \ , B-H, B, where H = (B-A)/(N-1).
#
#    real A, B, the limits of integration.
#
#    real T, multiplier of the X argument of the sine.
#
#  Output:
#
#    real VALUE, the approximate value of the integral.
#
  import numpy as np

  if ( a == b ):
    value = 0.0
    return value
 
  if ( n <= 1 ):
    print ( '' )
    print ( 'filon_tab_sin(): Fatal error!' )
    print ( '  N < 2' )
    print ( '  N = ', n )
    raise Exception ( 'filon_tab_sin(): Fatal error!' )
 
  if ( ( n % 2 ) != 1 ):
    print ( '' )
    print ( 'filon_tab_sin(): Fatal error!' )
    print ( '  N must be odd.' )
    print ( '  N = ', n )
    raise Exception ( 'filon_tab_sin(): Fatal error!' )
#
#  Set the X values.
#
  x = np.linspace ( a, b, n )
  h = ( b - a ) / ( n - 1 )
  theta = t * h

  sint = np.sin ( theta )
  cost = np.cos ( theta )

  if ( 6.0 * np.abs ( theta ) <= 1.0 ):

    alpha = 2.0 * theta**3 /   45.0 \
          - 2.0 * theta**5 /  315.0 \
          + 2.0 * theta**7 / 4725.0
  
    beta =  2.0           /     3.0 \
          + 2.0 * theta**2 /    15.0 \
          - 4.0 * theta**4 /   105.0 \
          + 2.0 * theta**6 /   567.0 \
          - 4.0 * theta**8 / 22275.0

    gamma = 4.0           /      3.0 \
          - 2.0 * theta**2 /     15.0 \
          +       theta**4 /    210.0 \
          -       theta**6 /  11340.0

  else:
 
    alpha = ( theta**2 + theta * sint * cost \
      - 2.0 * sint**2 ) / theta**3

    beta = ( 2.0 * theta + 2.0 * theta * cost**2 \
      - 4.0 * sint * cost ) / theta**3

    gamma = 4.0 * ( sint - theta * cost ) / theta**3
   
  s2n = np.sum ( ftab[0:n:2] * np.sin ( t * x[0:n:2] ) ) \
    - 0.5 * ( ftab[n-1] * np.sin ( t * x[n-1] ) \
            + ftab[0] * np.sin ( t * x[0] ) )

  s2nm1 = np.sum ( ftab[1:n-1:2] * np.sin ( t * x[1:n-1:2] ) )

  value = h * ( \
      alpha * ( ftab[0] * np.cos ( t * x[0] ) \
              - ftab[n-1] * np.cos ( t * x[n-1] ) ) \
    + beta * s2n \
    + gamma * s2nm1 )
 
  return value

def filon_test01 ( ):

#*****************************************************************************80
#
## filon_test01() tests filon_tab_cos().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  a = 0.0
  b = 2.0 * np.pi
  n = 11
#
#  Set the X values.
#
  x = np.linspace ( a, b, n )

  print ( '' )
  print ( 'filon_test01' )
  print ( '  FILON_TAB_COS estimates the integral of.' )
  print ( '  F(X) * COS ( T * X )' )
  print ( '  Use integrands F(X)=1, X, X**2.' )
  print ( '' )
  print ( '  A = ', a )
  print ( '  B = ', b )
  print ( '  N = ', n )
  print ( '' )
  print ( '       T        Approximate             Exact' )

  for k in range ( 1, 4 ):

    if ( k == 1 ):
      t = 1.0
    elif ( k == 2 ):
      t = 2.0
    elif ( k == 3 ):
      t = 10.0

    print ( '' )

    for i in range ( 1, 4 ):

      if ( i == 1 ):
        ftab = zero_integrand ( n, x )
      elif ( i == 2 ):
        ftab = one_integrand ( n, x )
      elif ( i == 3 ):
        ftab = two_integrand ( n, x )

      result = filon_tab_cos ( n, ftab, a, b, t )

      if ( i == 1 ):
        exact = ( np.sin ( t * b ) - np.sin ( t * a ) ) / t
      elif ( i == 2 ):
        exact = ( ( np.cos ( t * b ) + t * b * np.sin ( t * b ) ) \
                - ( np.cos ( t * a ) + t * a * np.sin ( t * a ) ) ) / t**2
      elif ( i == 3 ):
        exact = ( ( 2.0 * t * b * np.cos ( t * b ) \
              + ( t * t * b**2 - 2.0 ) * np.sin ( t * b ) ) \
                - ( 2.0 * t * a * np.cos ( t * a ) \
              + ( t * t * a**2 - 2.0 ) * np.sin ( t * a ) ) ) / t**3

      print ( '  %10.4g  %24.16g  %24.16g' % ( t, result, exact ) )

  return

def filon_test02 ( ):

#*****************************************************************************80
#
## filon_test02() tests filon_tab_cos().
#
#  Discussion:
#
#    Example suggested by James Roedder.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'filon_test02():' )
  print ( '  Integrate F(X) = log(1+X)*cos(T*X):' )
  print ( '  Supply integrand as a table.' )
  print ( '  T = 10, and N increases' )
  print ( '' )
  print ( '       N    Approximate             Exact                   Error' )
  print ( '' )

  a = 0.0
  b = 2.0 * np.pi

  for j in range ( 1, 7 ):

    n = 2 ** j * 10 + 1
#
#  Set the X values.
#
    x = np.linspace ( a, b, n )
    ftab = log_integrand ( n, x )
 
    t = 10.0
    result = filon_tab_cos ( n, ftab, a, b, t )

    exact = -0.008446594405
    error = result - exact

    print ( '  %6d  %22.16g  %22.16g  %10.4e' \
      % ( n, result, exact, error ) )

  return

def filon_test03 ( ):

#*****************************************************************************80
#
## filon_test03() tests filon_fun_cos().
#
#  Discussion:
#
#    Example suggested by James Roedder.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'filon_test03():' )
  print ( '  Integrate F(X)=log(1+X)*cos(T*X):' )
  print ( '  Supply integrand as a function.' )
  print ( '  T = 10, and N increases' )
  print ( '' )
  print ( '       N    Approximate             Exact                   Error' )
  print ( '' )

  a = 0.0
  b = 2.0 * np.pi

  for j in range ( 1, 7 ):

    n = 2 ** j * 10 + 1
 
    t = 10.0

    result = filon_fun_cos ( n, log_integrand, a, b, t )

    exact = -0.008446594405
    error = result - exact

    print ( '  %6d  %22.16g  %22.16g  %10.4e'  \
      % ( n, result, exact, error ) )

  return

def filon_test04 ( ):

#*****************************************************************************80
#
## filon_test04() tests filon_tab_sin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  a = 0.0
  b = 2.0 * np.pi
  n = 11
  x = np.linspace ( a, b, n )

  print ( '' )
  print ( 'filon_test04' )
  print ( '  FILON_TAB_SIN estimates the integral of.' )
  print ( '  F(X) * SIN ( T * X )' )
  print ( '  Use integrands 1, X, X**2.' )
  print ( '' )
  print ( '  A = ', a )
  print ( '  B = ', b )
  print ( '  N = ', n )
  print ( '' )
  print ( '           T        Approximate             Exact' )
  print ( '' )

  for k in range ( 1, 4 ):

    if ( k == 1 ):
      t = 1.0
    elif ( k == 2 ):
      t = 2.0
    elif ( k == 3 ):
      t = 10.0

    print ( '' )

    for i in range ( 1, 4 ):

      if ( i == 1 ):
        ftab = zero_integrand ( n, x )
      elif ( i == 2 ):
        ftab = one_integrand ( n, x )
      elif ( i == 3 ):
        ftab = two_integrand ( n, x )

      result = filon_tab_sin ( n, ftab, a, b, t )

      if ( i == 1 ):
        exact = ( - np.cos ( t * b ) + np.cos ( t * a ) ) / t
      elif ( i == 2 ):
        exact = ( ( np.sin ( t * b ) - t * b * np.cos ( t * b ) ) \
                - ( np.sin ( t * a ) - t * a * np.cos ( t * a ) ) ) / t**2
      elif ( i == 3 ):
        exact = ( ( 2.0 * t * b * np.sin ( t * b ) \
                + ( 2.0 - t**2 * b**2 ) * np.cos ( t * b ) ) \
                - ( 2.0 * t * a * np.sin ( t * a ) \
                + ( 2.0 - t**2 * a**2 ) * np.cos ( t * a ) ) ) / t**3

      print ( '  %10.4g  %24.16g  %24.16g' % ( t, result, exact ) )

  return

def filon_test05 ( ):

#*****************************************************************************80
#
## filon_test05() tests filon_tab_cos().
#
#  Discussion:
#
#    Example suggested by James Roedder.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'filon_test05():' )
  print ( '  Integrate F(X)=log(1+X)*sin(T*X):' )
  print ( '  Supply integrand as a table.' )
  print ( '  T = 10, and N increases' )
  print ( '' )
  print ( '       N    Approximate             Exact                   Error' )
  print ( '' )

  a = 0.0
  b = 2.0 * np.pi

  for j in range ( 1, 7 ):

    n = 2 ** j * 10 + 1
    x = np.linspace ( a, b, n )
    ftab = log_integrand ( n, x )

    t = 10.0

    result = filon_tab_sin ( n, ftab, a, b, t )

    exact = -0.19762680771872
    error = result - exact

    print ( '  %6d  %22.16g  %22.16g  %10.4e' \
      % ( n, result, exact, error ) )

  return

def filon_test06 ( ):

#*****************************************************************************80
#
## filon_test06() tests filon_fun_cos().
#
#  Discussion:
#
#    Example suggested by James Roedder.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'filon_test06():' )
  print ( '  Integrate F(X)=log(1+X)*sin(T*X):' )
  print ( '  Supply integrand as a function.' )
  print ( '  T = 10, and N increases' )
  print ( '' )
  print ( '       N    Approximate             Exact                   Error' )
  print ( '' )

  a = 0.0
  b = 2.0 * np.pi

  for j in range ( 1, 7 ):

    n = 2 ** j * 10 + 1

    t = 10.0
    result = filon_fun_sin ( n, log_integrand, a, b, t )

    exact = -0.19762680771872
    error = result - exact

    print ( '  %6d  %22.16g  %22.16g  %10.4e' \
      % ( n, result, exact, error ) )

  return

def log_integrand ( n, x ):

#*****************************************************************************80
#
## log_integrand() evaluates the logarithmic integrand.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    real X[n-1], the evaluation points.
#
#  Output:
#
#    real FX[n-1], the function values.
#
  import numpy as np

  fx = np.log ( 1.0 + x )

  return fx

def one_integrand ( n, x ):

#*****************************************************************************80
#
## one_integrand() evaluates the integrand X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    real X[n-1], the evaluation points.
#
#  Output:
#
#    real FX[n-1], the function values.
#
  fx = x.copy ( )

  return fx

def two_integrand ( n, x ):

#*****************************************************************************80
#
## two_integrand() evaluates the integrand X**2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    real X[n-1], the evaluation points.
#
#  Output:
#
#    real FX[n-1], the function values.
#
  fx = x ** 2

  return fx

def zero_integrand ( n, x ):

#*****************************************************************************80
#
## zero_integrand() evaluates the integrand x^0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    real X[n-1], the evaluation points.
#
#  Output:
#
#    real FX[n-1], the function values.
#
  import numpy as np

  fx = np.ones_like ( x )

  return fx

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
  filon_rule_test ( )
  timestamp ( )

