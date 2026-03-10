#! /usr/bin/env python3
#
def fresnel_test ( ):

#*****************************************************************************80
#
## fresnel_test() tests fresnel().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 July 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'fresnel_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  Test fresnel().' )

  fresnel_cos_values_test ( )
  fresnel_sin_values_test ( )
  fresnel_cos_plot ( )
  fresnel_sin_plot ( )
  fresnel_phase_plot ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'fresnel_test():' )
  print ( '  Normal end of execution.' )

  return

def fresnel_cos ( x ):

#*****************************************************************************80
#
## fresnel_cos() evaluates the Fresnel cosine integral C(x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 July 2025
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Shanjie Zhang, Jianming Jin,
#    Computation of Special Functions,
#    Wiley, 1996,
#    ISBN: 0-471-11963-6,
#    LC: QA351.C45.
#
#  Input:
#
#    real X: the argument.
#
#  Output:
#
#    real C: the Fresnel cosine integral value at X.
#
  c, s = fresnel ( x )

  return c

def fresnel ( x ):

#*****************************************************************************80
#
## fresnel() computes Fresnel integrals C(x) and S(x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 July 2025
#
#  Author:
#
#    Original Fortran77 version by Shanjie Zhang, Jianming Jin.
#    This version by John Burkardt.
#
#  Reference:
#
#    John D Cook,
#    Cornu's spiral,
#    Posted 23 March 2016.
#    https://www.johndcook.com/blog/2016/03/23/cornus-spiral/
#
#    Shanjie Zhang, Jianming Jin,
#    Computation of Special Functions,
#    Wiley, 1996,
#    ISBN: 0-471-11963-6,
#    LC: QA351.C45.
#
#  Input:
#
#    real X: the argument.
#
#  Output:
#
#    real C, S: the values of the Fresnel cosine and sine integrals.
#
  from math import floor
  import numpy as np

  eps = 1.0E-15
  xa = np.abs ( x )
  px = np.pi * xa
  t = 0.5 * px * xa
  t2 = t * t
#
#  x == 0
#
  if ( xa == 0.0 ):

    c = 0.0
    s = 0.0
#
#  0 < x < 2.5
#
  elif ( xa < 2.5 ):

    r = xa
    c = r
    for k in range ( 1, 51 ):
      r = -0.5 * r * ( 4.0 * k - 3.0 ) / k \
        / ( 2.0 * k - 1.0 ) / ( 4.0 * k + 1.0 ) * t2
      c = c + r
      if ( np.abs ( r ) < np.abs ( c ) * eps ):
        break

    s = xa * t / 3.0
    r = s
    for k in range ( 1, 51 ):
      r = - 0.5 * r * ( 4.0 * k - 1.0 ) / k \
        / ( 2.0 * k + 1.0 ) / ( 4.0 * k + 3.0 ) * t2
      s = s + r
      if ( np.abs ( r ) < np.abs ( s ) * eps ):
        if ( x < 0.0 ):
          c = -c
          s = -s
        return c, s
#
#  2.5 <= x < 4.5
#
  elif ( xa < 4.5 ):

    m = floor ( 42.0 + 1.75 * t )
    su = 0.0
    c = 0.0
    s = 0.0
    f1 = 0.0
    f0 = 1.0E-100

    for k in range ( m, -1, -1 ):
      f = ( 2.0 * k + 3.0 ) * f0 / t - f1
      if ( k % 2 == 0 ):
        c = c + f
      else:
        s = s + f
      su = su + ( 2.0 * k + 1.0 ) * f * f
      f1 = f0
      f0 = f

    q = np.sqrt ( su )
    c = c * xa / q
    s = s * xa / q
#
#  4.5 <= x
#
  else:

    r = 1.0
    f = 1.0
    for k in range ( 1, 21 ):
      r = -0.25 * r * ( 4.0 * k - 1.0 ) * ( 4.0 * k - 3.0 ) / t2
      f = f + r
    r = 1.0 / ( px * xa )
    g = r
    for k in range ( 1, 13 ):
      r = -0.25 * r * ( 4.0 * k + 1.0 ) * ( 4.0 * k - 1.0 ) / t2
      g = g + r
 
    t0 = t - floor ( t / ( 2.0 * np.pi ) ) * 2.0 * np.pi
    c = 0.5 + ( f * np.sin ( t0 ) - g * np.cos ( t0 ) ) / px
    s = 0.5 - ( f * np.cos ( t0 ) + g * np.sin ( t0 ) ) / px
#
#  Apply symmetry for x < 0.
#
  if ( x < 0.0 ):
    c = -c
    s = -s

  return c, s

def fresnel_sin ( x ):

#*****************************************************************************80
#
## fresnel_sin() evaluates the Fresnel sine integral S(x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 July 2025
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Shanjie Zhang, Jianming Jin,
#    Computation of Special Functions,
#    Wiley, 1996,
#    ISBN: 0-471-11963-6,
#    LC: QA351.C45.
#
#  Input:
#
#    real X: the argument.
#
#  Output:
#
#    real S: the Fresnel sine integral value at X.
#
  c, s = fresnel ( x )

  return s

def fresnel_cos_plot ( ):

#*****************************************************************************80
#
## fresnel_cos_plot() tests fresnel_cos().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 July 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'fresnel_cos_plot():' )
  print ( '  Plot (X,C(X)), where C(X) is the Fresnel cosine integral.' )

  a = -5.0
  b = +5.0
  n = 501
  x = np.linspace ( a, b, n )
  y = np.zeros ( n )

  for i in range ( 0, n ):
    y[i] = fresnel_cos ( x[i] )

  plt.clf ( )
  plt.plot ( x, y, 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- X -->' )
  plt.ylabel ( '<-- C(X) -->' )
  plt.title ( 'C(X) = Fresnel cosine integral' )
  filename = 'fresnel_cos_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def fresnel_cos_values ( n_data ):

#*****************************************************************************80
#
## fresnel_cos_values() returns values of the Fresnel cosine integral function.
#
#  Discussion:
#
#    The Fresnel cosine integral is defined by:
#
#      C(X) = integral ( 0 <= T <= X ) cos ( PI * T^2 / 2 ) dT
#
#    In Mathematica, the function can be evaluated by:
#
#      FresnelC[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2015
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
#  Input:
#
#    integer n_data.  The user sets n_data to 0 before the first call.  
#
#  Output:
#
#    integer n_data.  On each call, the routine increments n_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of n_data will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 16

  fx_vec = np.array ( ( \
     0.0000000000000000E+00, \
     0.1999210575944531E+00, \
     0.3974807591723594E+00, \
     0.5810954469916523E+00, \
     0.7228441718963561E+00, \
     0.7798934003768228E+00, \
     0.7154377229230734E+00, \
     0.5430957835462564E+00, \
     0.3654616834404877E+00, \
     0.3336329272215571E+00, \
     0.4882534060753408E+00, \
     0.6362860449033195E+00, \
     0.5549614058564281E+00, \
     0.3889374961919690E+00, \
     0.4674916516989059E+00, \
     0.6057207892976856E+00 ))

  x_vec = np.array ( ( \
     0.0E+00, \
     0.2E+00, \
     0.4E+00, \
     0.6E+00, \
     0.8E+00, \
     1.0E+00, \
     1.2E+00, \
     1.4E+00, \
     1.6E+00, \
     1.8E+00, \
     2.0E+00, \
     2.2E+00, \
     2.4E+00, \
     2.6E+00, \
     2.8E+00, \
     3.0E+00 ))

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

def fresnel_cos_values_test ( ):

#*****************************************************************************80
#
## fresnel_cos_values_test() tests fresnel_cos().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'fresnel_cos_values_test():' )
  print ( '  fresnel_cos_values() stores values of' )
  print ( '  the Fresnel cosine integral C(X).' )
  print ( '  fresnel_cos(x) computes the value directly.' )
  print ( '' )
  print ( '        X               C(X)                      C(X)' )
  print ( '                        Tabulated                 Computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = fresnel_cos_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = fresnel_cos ( x )

    print ( '  %12f  %24.16f  %24.16f' % ( x, fx1, fx2 ) )

  return

def fresnel_phase_plot ( ):

#*****************************************************************************80
#
## fresnel_phase_plot() tests fresnel_cos() and fresnel_sin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 July 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'fresnel_phase_plot():' )
  print ( '  Plot (C(X),S(X)), where C(X) and S(X) are ' )
  print ( '  the Fresnel cosine and sine integrals.' )

  a = -5.0
  b = +5.0
  n = 501
  x = np.linspace ( a, b, n )
  c = np.zeros ( n )
  s = np.zeros ( n )

  for i in range ( 0, n ):
    c[i] = fresnel_cos ( x[i] )
    s[i] = fresnel_sin ( x[i] )

  plt.clf ( )
  plt.plot ( c, s, 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- C(X) -->' )
  plt.ylabel ( '<-- S(X) -->' )
  plt.title ( 'Fresnel Phase Plot' )
  filename = 'fresnel_phase_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def fresnel_sin_plot ( ):

#*****************************************************************************80
#
## fresnel_sin_plot() tests fresnel_sin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 July 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'fresnel_sin_plot():' )
  print ( '  Plot (X,S(X)), where S(X) is the Fresnel sine integral.' )

  a = -5.0
  b = +5.0
  n = 501
  x = np.linspace ( a, b, n )
  y = np.zeros ( n )

  for i in range ( 0, n ):
    y[i] = fresnel_sin ( x[i] )

  plt.clf ( )
  plt.plot ( x, y, 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- X -->' )
  plt.ylabel ( '<-- S(X) -->' )
  plt.title ( 'S(X) = Fresnel sine integral' )
  filename = 'fresnel_sin_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def fresnel_sin_values ( n_data ):

#*****************************************************************************80
#
## fresnel_sin_values() returns some values of the Fresnel sine integral function.
#
#  Discussion:
#
#    The Fresnel sine integral is defined by
#
#      S(X) = integral ( 0 <= T <= X ) sin ( pi * T^2 / 2 ) dT
#
#    In Mathematica, the function can be evaluated by:
#
#      FresnelS[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer n_data.  The user sets n_data to 0 before the first call.  
#
#  Output:
#
#    integer n_data.  On each call, the routine increments n_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of n_data will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 16

  f_vec = np.array ( ( \
     0.0000000000000000E+00, \
     0.4187609161656762E-02, \
     0.3335943266061318E-01, \
     0.1105402073593870E+00, \
     0.2493413930539178E+00, \
     0.4382591473903548E+00, \
     0.6234009185462497E+00, \
     0.7135250773634121E+00, \
     0.6388876835093809E+00, \
     0.4509387692675831E+00, \
     0.3434156783636982E+00, \
     0.4557046121246569E+00, \
     0.6196899649456836E+00, \
     0.5499893231527195E+00, \
     0.3915284435431718E+00, \
     0.4963129989673750E+00 ) )

  x_vec = np.array ( ( \
     0.0E+00, \
     0.2E+00, \
     0.4E+00, \
     0.6E+00, \
     0.8E+00, \
     1.0E+00, \
     1.2E+00, \
     1.4E+00, \
     1.6E+00, \
     1.8E+00, \
     2.0E+00, \
     2.2E+00, \
     2.4E+00, \
     2.6E+00, \
     2.8E+00, \
     3.0E+00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def fresnel_sin_values_test ( ):

#*****************************************************************************80
#
## fresnel_sin_values_test() tests fresnel_sin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 July 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'fresnel_sin_values_test():' )
  print ( '  fresnel_sin_values() stores values of' )
  print ( '  the Fresnel sine integral S(X).' )
  print ( '  fresnel_sin(x) computes the value directly.' )
  print ( '' )
  print ( '        X               S(X)                      S(X)' )
  print ( '                        Tabulated                 Computed' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = fresnel_sin_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = fresnel_sin ( x )

    print ( '  %12f  %24.16f  %24.16f' % ( x, fx1, fx2 ) )

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
  fresnel_test ( )
  timestamp ( )

