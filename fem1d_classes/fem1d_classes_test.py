#! /usr/bin/env python3
#
from fem1d_classes import *
from math import *

def fem1d_classes_test ( title, N, rhsfn, exactfn ):

#*****************************************************************************80
#
#  Purpose:
#
#    FEM1D_CLASSES_TEST demonstates the use of FEM1D_CLASSES to solve a PDE.
#
#  Discussion:
#
#    The PDE is defined for 0 < x < 1:
#      -u'' = f
#    with right hand side
#      f(x) = -(exact(x)'') 
#    and boundary conditions
#      u(0) = exact(0),
#      u(1) = exact(1).
#
#    For the exact solution:
#      exact(x) = x * ( 1 - x ) * exp ( x )
#    the boundary conditions are
#      u(0) = 0.0,
#      u(1) = 0.0
#    and the right hand side is:
#      f(x) = x * ( x + 3 ) * exp ( x )
#
#  Modified:
#
#    22 August 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( title )
  print ( '  Solve -u"=rhs on [0,1] using %d elements.' % ( N ) )
#
#  Set a mesh of N elements in [ xleft, xright ].
#
  xleft = 0.0
  xright = 1.0
  mesh = Mesh ( N, xleft, xright )
#
#  Define the shape functions associated with any element.
#
  sfns = Shapefns ( )
#
#  The mesh and shape functions define the function space V.
#
  V = FunctionSpace ( mesh, sfns )
#
#  Get the coordinates of the degrees of freedom.
#  Because we use quadratic Lagrange elements, there are 2*N+1 of them.
#
  x = V.dofpts()
#
#  Evaluate the exact solution at each node.
#  We need this to apply Dirichlet boundary conditions,
#  and to compare against the computed solution.
#
  exact = exactfn ( x )
#
#  Evaluate the right hand side of the PDE at each node.
#
  rhs = rhsfn ( x )
#
#  Compute b, the right hand side of the finite element system.
#
  b = V.int_phi ( rhs )
#
#  Compute A, the stiffness matrix.
#
  A = V.int_phi_phi ( derivative = [ True, True ] )
#
#  Modify the linear system to enforce the left boundary condition.
#
  A[0,0] = 1.0
  A[0,1:] = 0.0
  b[0] = exact[0]
#
#  Modify the linear system to enforce the right boundary condition.
#
  A[-1,-1] = 1.0
  A[-1,0:-1] = 0.0
  b[-1] = exact[-1]
#
#  Solve A*u=b.
#
  u = la.solve ( A, b )    
#
#  Print the exact and computed solutions at nodes 0 through 2*N.
#
  print ( '' )
  print ( '   I        X            U(exact)         U(comp)' )
  print ( '' )
  for i in range ( 2 * N + 1 ):
    print ( '  %2d  %10.4f  %14.6g  %14.6g' % ( i, x[i], exact[i], u[i] ) )
#
#  Compute the relative error.
#
  print ( '' )
  print ( '  Relative error = ', la.norm ( u - exact ) / la.norm ( exact ) )

  import matplotlib.pyplot as plt
  plt.plot ( x, u, 'b', x, exact, 'ro' )
  plt.grid ( )
  plt.title ( title )
  plt.savefig ( 'test01.png' )
  plt.show ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_CLASSES_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rhsfn = lambda x : x*(x+3)*e**x
  exactfn = lambda x :x*(1-x)*e**x
  fem1d_classes_test ( 'Test01', 10, rhsfn, exactfn )
  timestamp ( )


