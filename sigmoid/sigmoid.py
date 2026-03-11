#! /usr/bin/env python3
#
def sigmoid_test ( ):

#*****************************************************************************80
#
## sigmoid_test() tests sigmoid().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 May 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'sigmoid_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test sigmoid.' )

  sigmoid_coef_test ( )
  sigmoid_value_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'sigmoid_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )

  return

def sigmoid_coef ( n ):

#*****************************************************************************80
#
## sigmoid_coef(): sigmoid derivative expansion coefficients.
#
#  Discussion:
#
#    s(x) = 1 / ( 1 + exp ( - x ) )
#
#    s(x)^(n) = sum ( 1 <= j <= n + 1 ) coef(j) * s(x)^j 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 May 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joe McKenna,
#    Derivatives of the sigmoid function,
#    https://joepatmckenna.github.io/calculus/derivative/sigmoid#20function/linear#20albegra/2018/01/20/sigmoid-derivs/
#
#  Input:
#
#    integer n: the order of the derivative.
#    0 <= n.
#
#  Output:
#
#    real coef(n+2): the expansion coefficients.
#    coef(1) is always 0, and coef(2) is always 1.
#
  from scipy.special import comb
  import numpy as np

  coef = np.zeros ( n + 2 )

  for k in range ( 0, n + 1 ):
    cnk = 0.0
    mop = -1.0
    for j in range ( 0, k + 1 ):
      mop = - mop
      cnk = cnk + mop * ( j + 1 )**n * comb ( k, j )
    coef[k+1] = cnk

  return coef

def sigmoid_coef_test ( ):

#*****************************************************************************80
#
## sigmoid_coef_test() tests sigmoid_coef().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 May 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'sigmoid_coef_test():'  )
  print ( '  sigmoid_coef() returns the coefficients of' )
  print ( '  the expansion of the nth derivative of the sigmoid' )
  print ( '  function in terms of powers of the sigmoid function.' )

  for n in range ( 0, 5 ):

    coef = sigmoid_coef ( n )
    label = '  s^(' + str ( n ) + ')(x)'
    sigmoid_poly_print ( coef, label )

  return

def sigmoid_value ( n, x ):

#*****************************************************************************80
#
## sigmoid_value(): evaluate sigmoid derivative at x.
#
#  Discussion:
#
#    s(x) = 1 / ( 1 + exp ( - x ) )
#
#    s(x)^(n) = sum ( 1 <= j <= n + 1 ) coef(j) * s(x)^j 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 May 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joe McKenna,
#    Derivatives of the sigmoid function,
#    https://joepatmckenna.github.io/calculus/derivative/sigmoid#20function/linear#20albegra/2018/01/20/sigmoid-derivs/
#
#  Input:
#
#    integer n: the order of the derivative.
#
#    real x: the evaluation point.
#
#  Output:
#
#    real value: the value of s^(n)(x).
#
  from scipy.special import comb
  import numpy as np

  sig = 1.0 / ( 1.0 + np.exp ( - x ) )
  value = 0.0
  sigk = 1.0

  for k in range ( 0, n + 1 ):

    sigk = sigk * sig
    cnk = 0.0
    mop = -1.0

    for j in range ( 0, k + 1 ):
      mop = - mop
      cnk = cnk + mop * ( j + 1 )**n * comb ( k, j )

    value = value + cnk * sigk

  return value

def sigmoid_value_test ( ):

#*****************************************************************************80
#
## sigmoid_value_test() tests sigmoid_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 May 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'sigmoid_value_test():'  )
  print ( '  sigmoid_value() evaluates the nth derivative' )
  print ( '  of the sigmoid function at the location x.' )

  for n in range ( 0, 4 ):

    xvec = np.linspace ( -5.0, +5.0, 51 )
    yvec = np.zeros ( 51 )
    for i in range ( 0, 51 ):
      yvec[i] = sigmoid_value ( n, xvec[i] )

    plt.clf ( )
    plt.plot ( xvec, yvec, linewidth = 2 )
    plt.grid ( True )
    plt.xlabel ( '<-- x -->' )
    plt.ylabel ( '<-- s(x) -->' )
    s = str ( n ) + ' derivative of sigmoid function'
    plt.title ( s )
    filename = 'sigmoid_' + str ( n ) + '.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )

  return

def sigmoid_poly_print ( a, title ):

#*****************************************************************************80
#
## ## sigmoid_poly_print() prints a polynomial in the sigmoid function s(x).
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A[M+1], the polynomial coefficients.
#    A[0] is the constant term and
#    A[M] is the coefficient of X^M.
#
#    string TITLE, a title.
#
  import numpy as np

  m = len ( a ) - 1

  if ( np.all ( a == 0.0 ) ):
    print ( label + ' = 0' )
    return
 
  first = True

  for i in range ( 0, m + 1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0.0 ):

      if ( first ):
        print ( title + ' =', end = '' )
        if ( plus_minus == '+' ):
          plus_minus = ' '
        first = False

      if ( 2 <= i ):
        print ( ' %c %g * s(x)^%d' % ( plus_minus, mag, i ), end = '' )
      elif ( i == 1 ):
        print ( ' %c %g * s(x)' % ( plus_minus, mag ), end = '' )
      elif ( i == 0 ):
        print ( ' %c %g' % ( plus_minus, mag ), end = '' )

  print ( '' )

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
  sigmoid_test ( )
  timestamp ( )

