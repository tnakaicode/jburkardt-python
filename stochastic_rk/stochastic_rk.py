#! /usr/bin/env python3
#
def stochastic_rk_test ( ):

#*****************************************************************************80
#
## stochastic_rk_test() tests stochastic_rk().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2025
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'stochastic_rk_test():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Test stochastic_rk().' )
#
#  Test rk1_ti_step().
#
  print ( '' )
  print ( '  rk1_ti_step() uses a first order RK method' )
  print ( '  for a problem whose right hand side does not' )
  print ( '  depend explicitly on time.' )

  rng = default_rng ( )

  n = 10
  t0 = 0.0
  tn = 1.0
  t, x = rk1_ti_step_test ( n, t0, tn, fi, gi, rng )
  print ( '' )
  print ( '         I           T             X' )
  print ( '' )
  for i in range ( 0, n + 1 ):
    print ( '  %8d  %14f  %14e' % ( i, t[i], x[i] ) )

  n = 100
  t0 = 0.0
  tn = 1.0
  t, x = rk1_ti_step_test ( n, t0, tn, fi, gi, rng )
  plt.clf ( )
  plt.plot ( t, x, 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.title ( 'stochastic ODE solution via rk1_ti_step()' )
  filename = 'rk1_ti_step_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'stochastic_rk_test():' )
  print ( '  Normal end of execution.' )

  return

def fi ( x ):

#*****************************************************************************80
#
## fi() is a time invariant deterministic right hand side.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the value.
#
  value = 1.0

  return value

def gi ( x ):

#*****************************************************************************80
#
## gi() is a time invariant stochastic right hand side.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the value.
#
  value = 1.0

  return value

def rk1_ti_step ( x, t, h, q, fi, gi, rng ):

#*****************************************************************************80
#
## rk1_ti_step() takes one step of a stochastic Runge Kutta scheme.
#
#  Discussion:
#
#    The Runge-Kutta scheme is first-order, and suitable for time-invariant
#    systems in which F and G do not depend explicitly on time.
#
#    d/dx X(t,xsi) = F ( X(t,xsi) ) + G ( X(t,xsi) ) * w(t,xsi)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jeremy Kasdin,
#    Runge-Kutta algorithm for the numerical integration of
#    stochastic differential equations,
#    Journal of Guidance, Control, and Dynamics,
#    Volume 18, Number 1, January-February 1995, pages 114-120.
#
#    Jeremy Kasdin,
#    Discrete Simulation of Colored Noise and Stochastic Processes
#    and 1/f^a Power Law Noise Generation,
#    Proceedings of the IEEE,
#    Volume 83, Number 5, 1995, pages 802-827.
#
#  Input:
#
#    real X, the value at the current time.
#
#    real T, the current time.
#
#    real H, the time step.
#
#    real Q, the spectral density of the input white noise.
#
#    external real FI, the name of the deterministic
#    right hand side function.
#
#    external real GI, the name of the stochastic
#    right hand side function.
#
#  Output:
#
#    real XSTAR, the value at time T+H.
#
  import numpy as np

  a21 = 1.0

  q1 = 1.0

  t1 = t
  x1 = x
  n1 = rng.standard_normal ( )
  w1 = n1 * np.sqrt ( q1 * q / h )
  k1 = h * fi ( x1 ) + h * gi ( x1 ) * w1

  xstar = x1 + a21 * k1

  return xstar

def rk1_ti_step_test ( n, t0, tn, fi, gi, rng ):

#*****************************************************************************80
#
## rk1_ti_step_test() tests rk1_ti_step().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  h = ( tn - t0 ) / n
  q = 1.0

  t = np.linspace ( t0, tn, n + 1 )
  x = np.zeros ( n + 1 )

  x[0] = 0.0
  for i in range ( 0, n ):
    x[i+1] = rk1_ti_step ( x[i], t[i], h, q, fi, gi, rng )

  return t, x

def rk1_tv_step ( x, t, h, q, fv, gv, rng ):

#*****************************************************************************80
#
## rk1_tv_step() takes one step of a stochastic Runge Kutta scheme.
#
#  Discussion:
#
#    The Runge-Kutta scheme is first-order, and suitable for time-varying
#    systems.
#
#    d/dx X(t,xsi) = F ( X(t,xsi), t ) + G ( X(t,xsi), t ) * w(t,xsi)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jeremy Kasdin,
#    Runge-Kutta algorithm for the numerical integration of
#    stochastic differential equations,
#    Journal of Guidance, Control, and Dynamics,
#    Volume 18, Number 1, January-February 1995, pages 114-120.
#
#    Jeremy Kasdin,
#    Discrete Simulation of Colored Noise and Stochastic Processes
#    and 1/f^a Power Law Noise Generation,
#    Proceedings of the IEEE,
#    Volume 83, Number 5, 1995, pages 802-827.
#
#  Input:
#
#    real X, the value at the current time.
#
#    real T, the current time.
#
#    real H, the time step.
#
#    real Q, the spectral density of the input white noise.
#
#    external real FV, the name of the deterministic
#    right hand side function.
#
#    external real GV, the name of the stochastic
#    right hand side function.
#
#  Output:
#
#    real XSTAR, the value at time T+H.
#
  import numpy as np

  a21 = 1.0

  q1 = 1.0

  t1 = t
  x1 = x
  n1 = rng.standard_normal ( )
  w1 = n1 * np.sqrt ( q1 * q / h )
  k1 = h * fv ( t1, x1 ) + h * gv ( t1, x1 ) * w1

  xstar = x1 + a21 * k1

  return xstar

def rk2_ti_step ( x, t, h, q, fi, gi, rng ):

#*****************************************************************************80
#
## rk2_ti_step() takes one step of a stochastic Runge Kutta scheme.
#
#  Discussion:
#
#    The Runge-Kutta scheme is second-order, and suitable for time-invariant
#    systems.
#
#    d/dx X(t,xsi) = F ( X(t,xsi) ) + G ( X(t,xsi) ) * w(t,xsi)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jeremy Kasdin,
#    Runge-Kutta algorithm for the numerical integration of
#    stochastic differential equations,
#    Journal of Guidance, Control, and Dynamics,
#    Volume 18, Number 1, January-February 1995, pages 114-120.
#
#    Jeremy Kasdin,
#    Discrete Simulation of Colored Noise and Stochastic Processes
#    and 1/f^a Power Law Noise Generation,
#    Proceedings of the IEEE,
#    Volume 83, Number 5, 1995, pages 802-827.
#
#  Input:
#
#    real X, the value at the current time.
#
#    real T, the current time.
#
#    real H, the time step.
#
#    real Q, the spectral density of the input white noise.
#
#    external real FI, the name of the deterministic
#    right hand side function.
#
#    external real GI, the name of the stochastic
#    right hand side function.
#
#  Output:
#
#    real XSTAR, the value at time T+H.
#
  import numpy as np

  a21 = 1.0
  a31 = 0.5
  a32 = 0.5

  q1 = 2.0
  q2 = 2.0

  t1 = t
  x1 = x
  n1 = rng.standard_normal ( )
  w1 = n1 * np.sqrt ( q1 * q / h )
  k1 = h * fi ( x1 ) + h * gi ( x1 ) * w1

  t2 = t1 + a21 * h
  x2 = x1 + a21 * k1
  n2 = rng.standard_normal ( )
  w2 = n2 * np.sqrt ( q2 * q / h )
  k2 = h * fi ( x2 ) + h * gi ( x2 ) * w2

  xstar = x1 + a31 * k1 + a32 * k2

  return xstar

def rk2_tv_step ( x, t, h, q, fv, gv, rng ):

#*****************************************************************************80
#
## rk2_tv_step() takes one step of a stochastic Runge Kutta scheme.
#
#  Discussion:
#
#    The Runge-Kutta scheme is second-order, and suitable for time-varying
#    systems.
#
#    d/dx X(t,xsi) = F ( X(t,xsi), t ) + G ( X(t,xsi), t ) * w(t,xsi)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jeremy Kasdin,
#    Runge-Kutta algorithm for the numerical integration of
#    stochastic differential equations,
#    Journal of Guidance, Control, and Dynamics,
#    Volume 18, Number 1, January-February 1995, pages 114-120.
#
#    Jeremy Kasdin,
#    Discrete Simulation of Colored Noise and Stochastic Processes
#    and 1/f^a Power Law Noise Generation,
#    Proceedings of the IEEE,
#    Volume 83, Number 5, 1995, pages 802-827.
#
#  Input:
#
#    real X, the value at the current time.
#
#    real T, the current time.
#
#    real H, the time step.
#
#    real Q, the spectral density of the input white noise.
#
#    external real FV, the name of the deterministic
#    right hand side function.
#
#    external real GV, the name of the stochastic
#    right hand side function.
#
#  Output:
#
#    real XSTAR, the value at time T+H.
#
  import numpy as np

  a21 = 1.0
  a31 = 0.5
  a32 = 0.5

  q1 = 2.0
  q2 = 2.0

  t1 = t
  x1 = x
  n1 = rng.standard_normal ( )
  w1 = n1 * np.sqrt ( q1 * q / h )
  k1 = h * fv ( t1, x1 ) + h * gv ( t1, x1 ) * w1

  t2 = t1 + a21 * h
  x2 = x1 + a21 * k1
  n2 = rng.standard_normal ( )
  w2 = n2 * np.sqrt ( q2 * q / h )
  k2 = h * fv ( t2, x2 ) + h * gv ( t2, x2 ) * w2

  xstar = x1 + a31 * k1 + a32 * k2

  return xstar

def rk3_ti_step ( x, t, h, q, fi, gi, rng ):

#*****************************************************************************80
#
## rk3_ti_step() takes one step of a stochastic Runge Kutta scheme.
#
#  Discussion:
#
#    The Runge-Kutta scheme is third-order, and suitable for time-invariant
#    systems in which F and G do not depend explicitly on time.
#
#    d/dx X(t,xsi) = F ( X(t,xsi) ) + G ( X(t,xsi) ) * w(t,xsi)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jeremy Kasdin,
#    Runge-Kutta algorithm for the numerical integration of
#    stochastic differential equations,
#    Journal of Guidance, Control, and Dynamics,
#    Volume 18, Number 1, January-February 1995, pages 114-120.
#
#    Jeremy Kasdin,
#    Discrete Simulation of Colored Noise and Stochastic Processes
#    and 1/f^a Power Law Noise Generation,
#    Proceedings of the IEEE,
#    Volume 83, Number 5, 1995, pages 802-827.
#
#  Input:
#
#    real X, the value at the current time.
#
#    real T, the current time.
#
#    real H, the time step.
#
#    real Q, the spectral density of the input white noise.
#
#    external real FI, the name of the deterministic
#    right hand side function.
#
#    external real GI, the name of the stochastic
#    right hand side function.
#
#  Output:
#
#    Output, real XSTAR, the value at time T+H.
#
  import numpy as np

  a21 = 1.52880952525675
  a31 = 0.0
  a32 = 0.51578733443615
  a41 = 0.53289582961739
  a42 = 0.25574324768195
  a43 = 0.21136092270067

  q1 = 1.87653936176981
  q2 = 3.91017166264989
  q3 = 4.73124353935667

  t1 = t
  x1 = x
  n1 = rng.standard_normal ( )
  w1 = n1 * np.sqrt ( q1 * q / h )
  k1 = h * fi ( x1 ) + h * gi ( x1 ) * w1

  t2 = t1 + a21 * h
  x2 = x1 + a21 * k1
  n2 = rng.standard_normal ( )
  w2 = n2 * np.sqrt ( q2 * q / h )
  k2 = h * fi ( x2 ) + h * gi ( x2 ) * w2

  t3 = t1 + a31 * h  + a32 * h
  x3 = x1 + a31 * k1 + a32 * k2
  n3 = rng.standard_normal ( )
  w3 = n3 * np.sqrt ( q3 * q / h )
  k3 = h * fi ( x3 ) + h * gi ( x3 ) * w3

  xstar = x1 + a41 * k1 + a42 * k2 + a43 * k3

  return xstar

def rk4_ti_step ( x, t, h, q, fi, gi, rng ):

#*****************************************************************************80
#
## rk4_ti_step() takes one step of a stochastic Runge Kutta scheme.
#
#  Discussion:
#
#    The Runge-Kutta scheme is fourth-order, and suitable for time-invariant
#    systems in which F and G do not depend explicitly on time.
#
#    d/dx X(t,xsi) = F ( X(t,xsi) ) + G ( X(t,xsi) ) * w(t,xsi)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jeremy Kasdin,
#    Runge-Kutta algorithm for the numerical integration of
#    stochastic differential equations,
#    Journal of Guidance, Control, and Dynamics,
#    Volume 18, Number 1, January-February 1995, pages 114-120.
#
#    Jeremy Kasdin,
#    Discrete Simulation of Colored Noise and Stochastic Processes
#    and 1/f^a Power Law Noise Generation,
#    Proceedings of the IEEE,
#    Volume 83, Number 5, 1995, pages 802-827.
#
#  Input:
#
#    real X, the value at the current time.
#
#    real T, the current time.
#
#    real H, the time step.
#
#    real Q, the spectral density of the input white noise.
#
#    external real FI, the name of the deterministic
#    right hand side function.
#
#    external real GI, the name of the stochastic
#    right hand side function.
#
#  Output:
#
#    real XSTAR, the value at time T+H.
#
  import numpy as np

  a21 =   2.71644396264860
  a31 = - 6.95653259006152
  a32 =   0.78313689457981
  a41 =   0.0
  a42 =   0.48257353309214
  a43 =   0.26171080165848
  a51 =   0.47012396888046
  a52 =   0.36597075368373
  a53 =   0.08906615686702
  a54 =   0.07483912056879

  q1 =   2.12709852335625
  q2 =   2.73245878238737
  q3 =  11.22760917474960
  q4 =  13.36199560336697

  t1 = t
  x1 = x
  n1 = rng.standard_normal ( )
  w1 = n1 * np.sqrt ( q1 * q / h )
  k1 = h * fi ( x1 ) + h * gi ( x1 ) * w1

  t2 = t1 + a21 * h
  x2 = x1 + a21 * k1
  n2 = rng.standard_normal ( )
  w2 = n2 * np.sqrt ( q2 * q / h )
  k2 = h * fi ( x2 ) + h * gi ( x2 ) * w2

  t3 = t1 + a31 * h  + a32 * h
  x3 = x1 + a31 * k1 + a32 * k2
  n3 = rng.standard_normal ( )
  w3 = n3 * np.sqrt ( q3 * q / h )
  k3 = h * fi ( x3 ) + h * gi ( x3 ) * w3

  t4 = t1 + a41 * h  + a42 * h + a43 * h
  x4 = x1 + a41 * k1 + a42 * k2
  n4 = rng.standard_normal ( )
  w4 = n4 * np.sqrt ( q4 * q / h )
  k4 = h * fi ( x4 ) + h * gi ( x4 ) * w4

  xstar = x1 + a51 * k1 + a52 * k2 + a53 * k3 + a54 * k4

  return xstar

def rk4_tv_step ( x, t, h, q, fv, gv, rng ):

#*****************************************************************************80
#
## rk4_tv_step() takes one step of a stochastic Runge Kutta scheme.
#
#  Discussion:
#
#    The Runge-Kutta scheme is fourth-order, and suitable for time-varying
#    systems.
#
#    d/dx X(t,xsi) = F ( X(t,xsi), t ) + G ( X(t,xsi), t ) * w(t,xsi)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 September 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jeremy Kasdin,
#    Runge-Kutta algorithm for the numerical integration of
#    stochastic differential equations,
#    Journal of Guidance, Control, and Dynamics,
#    Volume 18, Number 1, January-February 1995, pages 114-120.
#
#    Jeremy Kasdin,
#    Discrete Simulation of Colored Noise and Stochastic Processes
#    and 1/f^a Power Law Noise Generation,
#    Proceedings of the IEEE,
#    Volume 83, Number 5, 1995, pages 802-827.
#
#  Input:
#
#    real X, the value at the current time.
#
#    real T, the current time.
#
#    real H, the time step.
#
#    real Q, the spectral density of the input white noise.
#
#    external real FV, the deterministic right hand side function.
#
#    external real GV, the stochastic right hand side function.
#
#  Output:
#
#    real XSTAR, the value at time T+H.
#
  import numpy as np

  a21 =   0.66667754298442
  a31 =   0.63493935027993
  a32 =   0.00342761715422
  a41 = - 2.32428921184321
  a42 =   2.69723745129487
  a43 =   0.29093673271592
  a51 =   0.25001351164789
  a52 =   0.67428574806272
  a53 = - 0.00831795169360
  a54 =   0.08401868181222

  q1 = 3.99956364361748
  q2 = 1.64524970733585
  q3 = 1.59330355118722
  q4 = 0.26330006501868

  t1 = t
  x1 = x
  n1 = rng.standard_normal ( )
  w1 = n1 * np.sqrt ( q1 * q / h )
  k1 = h * fv ( t1, x1 ) + h * gv ( t1, x1 ) * w1

  t2 = t1 + a21 * h
  x2 = x1 + a21 * k1
  n2 = rng.standard_normal ( )
  w2 = n2 * np.sqrt ( q2 * q / h )
  k2 = h * fv ( t2, x2 ) + h * gv ( t2, x2 ) * w2

  t3 = t1 + a31 * h  + a32 * h
  x3 = x1 + a31 * k1 + a32 * k2
  n3 = rng.standard_normal ( )
  w3 = n3 * np.sqrt ( q3 * q / h )
  k3 = h * fv ( t3, x3 ) + h * gv ( t3, x3 ) * w3

  t4 = t1 + a41 * h  + a42 * h  + a43 * h
  x4 = x1 + a41 * k1 + a42 * k2 + a43 * k3
  n4 = rng.standard_normal ( )
  w4 = n4 * np.sqrt ( q4 * q / h )
  k4 = h * fv ( t4, x4 ) + h * gv ( t4, x4 ) * w4

  xstar = x1 + a51 * k1 + a52 * k2 + a53 * k3 + a54 * k4

  return xstar

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
#    04 September 2025
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
  stochastic_rk_test ( )
  timestamp ( )

