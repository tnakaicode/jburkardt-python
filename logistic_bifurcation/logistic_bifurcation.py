#! /usr/bin/env python3
#
def logistic_attractors ( x, r ):

#*****************************************************************************80
#
## logistic_attractors finds the attractors for a particular logistic map.
#
#  Modified:
#
#    12 January 2020
#
#  Author:
#
#    John Cook
#
#  Reference:
#
#    John Cook,
#    Logistic bifurcation diagram in detail,
#    11 January 2020,
#    https://www.johndcook.com/blog/
#
#  Input:
#
#    real x, the starting iterate.
#
#    real r, the logistic parameter.
#
#  Output:
#
#    real ts(*), the set of attractors.
#
  x = logistic_iter ( x, r, 100 )
  x0 = round ( x, 4 )
  ts = { x0 }

  for c in range ( 1000 ):
    x = logistic_map ( x, r )
    xr = round ( x, 4 )
    if xr in ts:
      break
    else:
      ts.add ( xr )

  return ts

def logistic_map ( x, r ):

#*****************************************************************************80
#
## logistic_map evaluates the logistic map once.
#
#  Modified:
#
#    12 January 2020
#
#  Author:
#
#    John Cook
#
#  Reference:
#
#    John Cook,
#    Logistic bifurcation diagram in detail,
#    11 January 2020,
#    https://www.johndcook.com/blog/
#
#  Input:
#
#    real x, the current iterate.
#
#    real r, the logistic parameter.  Values 0 < r < 4 are of interest.
#
#  Output:
#
#    real value, the next iterate.
#    
  value = r * x * ( 1.0 - x )

  return value

def logistic_iter ( x, r, n ):

#*****************************************************************************80
#
## logistic_iter evaluates the logistic map n times.
#
#  Modified:
#
#    12 January 2020
#
#  Author:
#
#    John Cook
#
#  Reference:
#
#    John Cook,
#    Logistic bifurcation diagram in detail,
#    11 January 2020,
#    https://www.johndcook.com/blog/
#
#  Input:
#
#    real x, the starting iterate.
#
#    real r, the logistic parameter.  Values 0 < r < 4 are of interest.
#
#    integer n, the number of iterations to apply.
#
#  Output:
#
#    real value, the n-th iterate.
#    
  for _ in range ( n ):
    x = logistic_map ( x, r )

  return x

def logistic_bifurcation_test ( ):

#*****************************************************************************80
#
## logistic_bifurcation_test tests logistic_bifurcation.
#
#  Modified:
#
#    12 January 2020
#
#  Author:
#
#    John Cook
#
#  Reference:
#
#    John Cook,
#    Logistic bifurcation diagram in detail,
#    11 January 2020,
#    https://www.johndcook.com/blog/
#
  import numpy as np
  import matplotlib.pyplot as plt
  import platform

  print ( '' )
  print ( 'logistic_bifurcation_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Draw the logistic map bifurcation diagram.' )
#
#  Sample values of r between 0 and 4.
#
  rs = np.linspace ( 0, 4, 1000 )
#
#  For each r, compute ts, the set of attractors for the iteration.
#
  for r in rs:
    ts = logistic_attractors ( 0.1, r )
#
#  Plot r versus its attractors.
#
    for t in ts:
      plt.plot ( r, t, "ko", markersize = 1 )

  filename = 'logistic_bifurcation.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )

  plt.show ( block = False )

  print ( '' )
  print ( 'logistic_bifurcation_test:' )
  print ( '  Normal end of execution.' )

  return

if ( __name__ == '__main__' ):
  logistic_bifurcation_test ( )

