#! /usr/bin/env python3
#
def assemble_fem ( x_num, x, element_num, element_node, quad_num, t, k_fun, \
  rhs_fun ):

#*****************************************************************************80
#
## ASSEMBLE_FEM assembles the finite element stiffness matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real X(X_NUM), the coordinates of nodes.
#
#    Input, integer ELEMENT_NUM, the number of elements.
#
#    Input, integer ELEMENT_NODE(2,ELEMENT_NUM);
#    ELEMENT_NODE(I,J) is the global index of local node I in element J.
#
#    Input, integer QUAD_NUM, the number of quadrature points used in assembly.
#
#    Input, real T, the current time.
#
#    Input, real K_FUN(), a function to evaluate the heat conductivity.
#
#    Input, real RHS_FUN(), a function to evaluate the right hand side.
#
#    Output, sparse real A(X_NUM,X_NUM), the finite element stiffness matrix.
#
#    Output, real B(X_NUM), the right hand side.
#
#  Local parameters:
#
#    Local, real BI, DBIDX, the value of some basis function
#    and its first derivative at a quadrature point.
#
#    Local, real BJ, DBJDX, the value of another basis
#    function and its first derivative at a quadrature point.
#
  import numpy as np
#
#  Initialize the arrays.
#
  b = np.zeros ( x_num )
  a = np.zeros ( ( x_num, x_num ) )
#
#  Get the quadrature weights and nodes.
#
  reference_w, reference_q = quadrature_set ( quad_num )
#
#  Consider each ELEMENT.
#
  for element in range ( 0, element_num ):

    element_x = np.zeros ( 2 )
    element_x[0] = x[element_node[0,element]]
    element_x[1] = x[element_node[1,element]]

    element_q = reference_to_physical ( element, element_node, x, quad_num, \
      reference_q )

    element_area = element_x[1] - element_x[0]

    element_w = np.zeros ( quad_num )
    for quad in range ( 0, quad_num ):
      element_w[quad] = ( element_area / 2.0 ) * reference_w[quad]
#
#  Consider the QUAD-th quadrature point in the element.
#
    k_value = k_fun ( quad_num, element_q, t )
    rhs_value = rhs_fun ( quad_num, element_q, t )

    for quad in range ( 0, quad_num ):
#
#  Consider the TEST-th test function.
#
#  We generate an integral for every node associated with an unknown.
#
      for i in range ( 0, 2 ):

        test = element_node[i,element]

        bi, dbidx = basis_function ( test, element, x, element_q[quad] )

        b[test] = b[test] + element_w[quad] * rhs_value[quad] * bi
#
#  Consider the BASIS-th basis function, which is used to form the
#  value of the solution function.
#
        for j in range ( 0, 2 ):

          basis = element_node[j,element]

          bj, dbjdx = basis_function ( basis, element, x, element_q[quad] )

          a[test,basis] = a[test,basis] + element_w[quad] * ( \
            + k_value[quad] * dbidx * dbjdx )

  return a, b

def assemble_mass ( node_num, node_x, element_num, element_node, quad_num ):

#*****************************************************************************80
#
## ASSEMBLE_MASS assembles the finite element mass matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NODE_NUM, the number of nodes.
#
#    Input, real NODE_X(NODE_NUM), the coordinates of nodes.
#
#    Input, integer ELEMENT_NUM, the number of elements.
#
#    Input, integer ELEMENT_NODE(2,ELEMENT_NUM);
#    ELEMENT_NODE(I,J) is the global index of local node I in element J.
#
#    Input, integer QUAD_NUM, the number of quadrature points used in assembly.
#
#    Output, sparse real C(NODE_NUM,NODE_NUM), the finite element mass matrix.
#
#  Local parameters:
#
#    Local, real BI, DBIDX, the value of some basis function
#    and its first derivative at a quadrature point.
#
#    Local, real BJ, DBJDX, the value of another basis
#    function and its first derivative at a quadrature point.
#
  import numpy as np
#
#  Initialize the arrays.
#
  c = np.zeros ( ( node_num, node_num ) )
#
#  Get the quadrature weights and nodes.
#
  reference_w, reference_q = quadrature_set ( quad_num )
#
#  Consider each ELEMENT.
#
  for element in range ( 0, element_num ):

    element_x = np.zeros ( 2 )
    element_x[0] = node_x[element_node[0,element]]
    element_x[1] = node_x[element_node[1,element]]

    element_q = reference_to_physical ( element, element_node, node_x, \
      quad_num, reference_q )

    element_area = element_x[1] - element_x[0]

    element_w = np.zeros ( quad_num )
    for quad in range ( 0, quad_num ):
      element_w[quad] = ( element_area / 2.0 ) * reference_w[quad]
#
#  Consider the QUAD-th quadrature point in the element.
#
    for quad in range ( 0, quad_num ):
#
#  Consider the TEST-th test function.
#
#  We generate an integral for every node associated with an unknown.
#
      for i in range ( 0, 2 ):

        test = element_node[i,element]

        bi, dbidx = basis_function ( test, element, node_x, element_q[quad] )
#
#  Consider the BASIS-th basis function, which is used to form the
#  value of the solution function.
#
        for j in range ( 0, 2 ):

          basis = element_node[j,element]

          bj, dbjdx = basis_function ( basis, element, node_x, element_q[quad] )

          c[test,basis] = c[test,basis] + element_w[quad] * bi * bj

  return c

def basis_function ( index, element, node_x, point_x ):

#*****************************************************************************80
#
## BASIS_FUNCTION evaluates a basis function.
#
#  Discussion:
#
#    Piecewise linear basis functions are used.
#
#    Basis functions are associated with NODES, and are numbered 1 to NODE_NUM.
#
#    Elements are associated with intervals, having nodes as endpoints.
#    Element I begins at node I and ends at node I+1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer INDEX, the index of the basis function to be evaluated.
#
#    Input, integer ELEMENT, the index of the element in which the points lie.
#
#    Input, real NODE_X(NODE_NUM), the coordinates of nodes.
#
#    Input, integer POINT_NUM, the number of evaluation points.
#
#    Input, real POINT_X, the evaluation points.
#
#    Output, real B, DBDX, the basis function and its derivative, evaluated
#    at the evaluation points.
#
  import numpy as np

  b    = 0.0
  dbdx = 0.0

  if ( index == element ):
    b    = ( node_x[element+1] - point_x ) / ( node_x[element+1] - node_x[element] )
    dbdx =                     - 1.0       / ( node_x[element+1] - node_x[element] )
  elif ( index == element + 1 ):
    b    = ( point_x - node_x[element] )   / ( node_x[element+1] - node_x[element] )
    dbdx = + 1.0                           / ( node_x[element+1] - node_x[element] )

  return b, dbdx

def fem1d_heat_explicit_cfl ( x_num, k, x, dt ):

#*****************************************************************************80
#
## FEM1D_HEAT_EXPLICIT_CFL: compute the Courant-Friedrichs-Loewy coefficient.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 November 2014
#
#  Author:
# 
#    John Burkardt
#
#  Reference:
#
#    George Lindfield, John Penny,
#    Numerical Methods Using MATLAB,
#    Second Edition,
#    Prentice Hall, 1999,
#    ISBN: 0-13-012641-1,
#    LC: QA297.P45.
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real K(X_NUM), the heat conductivity coefficient.
#
#    Input, real NODE_X(X_NUM), the coordinates of the nodes.
#
#    Input, real DT, the time step.
#
#    Output, real CFL, the Courant-Friedrichs-Loewy coefficient.
#
  from sys import exit

  cfl = 0.0
  for i in range ( 0, x_num - 2 ):
    cfl = max ( cfl, 2.0 * k[i+1] / ( x[i+2] - x[i] ) ** 2 )
 
  cfl = dt * cfl

  if ( 0.5 <= cfl ):
    print ( '' )
    print ( 'FEM1D_HEAT_EXPLICIT_CFL - Fatal error!' )
    print ( '  CFL condition failed.' )
    print ( '  0.5 <= K * dT / dX / dX = %g' % ( cfl ) )
    exit ( 'FEM1D_HEAT_EXPLICIT_CFL - Fatal error!' )

  return cfl

def fem1d_heat_explicit_cfl_test ( ):

#*****************************************************************************80
#
## FEM1D_HEAT_EXPLICIT_CFL_TEST tests FEM1D_HEAT_EXPLICIT_CFL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'FEM1D_HEAT_EXPLICIT_CFL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FEM1D_HEAT_EXPLICIT_CFL evaluates the CFL parameter.' )

  x_num = 51
  k = np.zeros ( x_num )
  for i in range ( 0, x_num ):
    k[i] = 1.0
  node_x = np.linspace ( 0.0, 10.0, x_num )
  dt = 0.025

  cfl = fem1d_heat_explicit_cfl ( x_num, k, node_x, dt )

  print ( '' )
  print ( '  CFL = %g' % ( cfl ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_HEAT_EXPLICIT_CFL_TEST:' )
  print ( '  Normal end of execution.' )
  return
  
def fem1d_heat_explicit ( x_num, x, t, dt, k_fun, rhs_fun, bc_fun, \
  element_num, element_node, quad_num, mass, u ):

#*****************************************************************************80
#
## FEM1D_HEAT_EXPLICIT: finite element method, 1D heat, explicit time steps.
#
#  Discussion:
#
#    This program solves
#
#      dUdT - k * d2UdX2 = f(X,T)
#
#    over the space interval [A,B], with boundary conditions
#
#      U(A,T) = UA(T),
#      U(B,T) = UB(T),
#
#    and over the time interval [T0,T1], with initial conditions
#
#      U(X,T0) = U0(X)
#
#    and specified functions k(X,T) and f(X,T).
#
#    The code uses the finite element method to approximate the
#    second derivative in space, and an explicit forward Euler approximation
#    to the first derivative in time.
#
#    For a test function Vi, we write
#
#      dUdt Vi = k * d2Udx2 * Vi + f(x,t) * Vi
#
#      Int dUdt Vi = Int   k * d2Udx2 * Vi    + f(x,t) * Vi
#                  = Int - k * dUdx   * dVidx + f(x,t) * Vi
#
#    Take the forward Euler approximation to the derivative:
#
#      Int ( U(x,t+dt) - U(x,t) ) / dt * Vi = Int ( - k * dUdx * dVidx + f(x,t) * Vi )
#
#    Now, assume the finite element projection:
#
#      U(x,t)    = sum ( uj     * Vj )
#      U(x,t+dt) = sum ( u_newj * Vj )
#      F(x,t)    = sum ( fj     * Vj ):
#
#    Then the equation can be rewritten as:
#
#      Sum ( Int ( Vi Vj ) * ( u_newj - uj ) / dt ) = 
#                          Sum ( Int ( - k * dVidx dVjdx uj + Vi * Vj * fj ) )
#
#    and the collection of equations for all the Vi in our basis becomes:
#
#      M * ( dudt ) = ( - K * u + b )
#      u_new = u + dt * dudt
#
#    or, symbolically, as:
#
#      u_new = u + dt * inverse ( M ) * ( - K * u + b )
#
#    Here "M" is the standard finite element mass matrix, "K" is the standard 
#    finite element stiffness matrix, and "b" the standard finite element right 
#    hand side.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 February 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of points to use in the spatial dimension.
#
#    Input, real X(X_NUM), the coordinates of the nodes.
#
#    Input, real T, the current time.
#
#    Input, real DT, the size of the time step.
#
#    Input, real K_FUN(), a function to evaluate the heat conductivity.
#
#    Input, real RHS_FUN(), a function to evaluate the right hand side.
#
#    Input, real BC_FUN(), a function to set the Dirichlet conditions.
#
#    Input, integer ELEMENT_NUM, the number of elements.
#
#    Input, integer ELEMENT_NODE(2,ELEMENT_NUM), the nodes belonging to 
#    each element.
#
#    Input, integer QUAD_NUM, the number of quadrature points to use.
#
#    Input, sparse real MASS(NODE_NUM,NODE_NUM), the mass matrix.
#
#    Input, real U(X_NUM), the solution at time T.
#
#    Output, real U_NEW(X_NUM), the solution at time T + dT.
#
  import numpy as np
#
#  Check stability condition.
#
  k_vec = k_fun ( x_num, x, t )
  cfl = fem1d_heat_explicit_cfl ( x_num, k_vec, x, dt )
#
#  Compute the spatial finite element information.
#
  a, b = assemble_fem ( x_num, x, element_num, element_node, \
    quad_num, t, k_fun, rhs_fun )
#
#  The system we wnat to solve is
#
#    MASS * dudt = - A * u + b
#
#  Add "-A*u" to the right hand side;
#
  rhs = - np.dot ( a, u )
  for i in range ( 0, x_num ):
    rhs[i] = rhs[i] + b[i]
#
#  Now solve MASS * dudt = - A * u + b
#
  dudt = np.linalg.solve ( mass, rhs )
#
#  Set u_new = u + dt * dudt.
#
  u_new = np.zeros ( x_num )
  for i in range ( 0, x_num ):
    u_new[i] = u[i] + dt * dudt[i]
#
#  Impose boundary conditions on u_new.
#
  u_new = bc_fun ( x_num, x, t + dt, u_new )

  return u_new
 
def fem1d_heat_explicit_test01 ( ):

#*****************************************************************************80
#
## FEM1D_HEAT_EXPLICIT_TEST01 runs a simple test.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  from matplotlib.ticker import LinearLocator, FormatStrFormatter
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'FEM1D_HEAT_EXPLICIT_TEST01:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  The time dependent 1D heat equation is' )
  print ( '' )
  print ( '    Ut - k * Uxx = f(x,t)' )
  print ( '' )
  print ( '  for space interval A <= X <= B with boundary conditions' )
  print ( '' )
  print ( '    U(A,t) = UA(t)' )
  print ( '    U(B,t) = UB(t)' )
  print ( '' )
  print ( '  and time interval T0 <= T <= T1 with initial condition' )
  print ( '' )
  print ( '    U(X,T0) = U0(X).' )
  print ( '' )
  print ( '  To compute an approximate solution:' )
  print ( '    the interval [A,B] is replace by a discretized mesh Xi' )
  print ( '    a set of finite element functions PSI(X) are determined,' )
  print ( '    the solution U is written as a weighted sum of the basis functions,' )
  print ( '    the weak form of the differential equation is written,' )
  print ( '    a time grid Tj is imposed, and time derivatives replaced by' )
  print ( '    an explicit forward Euler first difference,' )
  print ( '' )
  print ( '    The continuous PDE has now been transformed into a set of algebraic' )
  print ( '    equations for the coefficients C(Xi,Tj).' )
#
#  Set the nodes.
#
  x_num = 21
  x_min = 0.0
  x_max = 1.0
  dx = ( x_max - x_min ) / ( x_num - 1 )
  x = np.linspace ( x_min, x_max, x_num )
#
#  Set the times.
#
  t_num = 401
  t_min = 0.0
  t_max = 80.0
  dt = ( t_max - t_min ) / ( t_num - 1 )
  t = np.linspace ( t_min, t_max, t_num )
#
#  Set finite element information.
#
  element_num = x_num - 1
  element_node = np.zeros ( [ 2, element_num ], dtype = np.int32 )
  for j in range ( 0, element_num ):
    element_node[0,j] = j
    element_node[1,j] = j + 1
  quad_num = 3
  mass = assemble_mass ( x_num, x, element_num, element_node, quad_num )

  print ( '' )
  print ( '  Number of X nodes = %d' % ( x_num ) )
  print ( '  X interval = [ %f, %f ]' % ( x_min, x_max ) )
  print ( '  X step size = %f' % ( dx ) )
  print ( '  Number of T steps = %d' % ( t_num ) )
  print ( '  T interval = [ %f, %f ]' % ( t_min, t_max ) )
  print ( '  T step size = %f' % ( dt ) )
  print ( '  Number of elements = %d' % ( element_num ) )
  print ( '  Number of quadrature points = %d' % ( quad_num ) )

  u_mat = np.zeros ( ( x_num, t_num ) )

  for j in range ( 0, t_num ):

    if ( j == 0 ):

      u = ic_test01 ( x_num, x, t[j] )
      u = bc_test01 ( x_num, x, t[j], u )

    else:

      u = fem1d_heat_explicit ( x_num, x, t[j-1], dt, k_test01, \
        rhs_test01, bc_test01, element_num, element_node, quad_num, mass, u )

    for i in range ( 0, x_num ):
      u_mat[i,j] = u[i]
#
#  Make a product grid of T and X for plotting.
#
  t_mat, x_mat = np.meshgrid ( t, x )
#
#  Make a mesh plot of the solution.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  surf = ax.plot_surface ( x_mat, t_mat, u_mat )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---T--->' )
  plt.title ( 'U(X,T)' )
  filename = 'plot_test01.png'
  plt.savefig ( filename )
  plt.show ( block = False )
#
#  Write the data to files.
#
  r8mat_write ( 'h_test01.txt', x_num, t_num, u_mat )
  r8vec_write ( 't_test01.txt', t_num, t )
  r8vec_write ( 'x_test01.txt', x_num, x )

  print ( '' )
  print ( '  H(X,T) written to "h_test01.txt"' )
  print ( '  T values written to "t_test01.txt"' )
  print ( '  X values written to "x_test01.txt"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_HEAT_EXPLICIT_TEST01:' )
  print ( '  Normal end of execution.' )
  return

def bc_test01 ( x_num, x, t, u ):

#*****************************************************************************80
#
## BC_TEST01 sets the boundary conditions for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 February 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real  X(X_NUM,1), the coordinates of the points.
#
#    Input, real T, the current time.
#
#    Input, real U(X_NUM), the solution at time T.
#
#    Output, real U(X_NUM), the solution at time T, with
#    boundary conditions enforced.
#
  u[0]       = 90.0
  u[x_num-1] = 70.0

  return u

def ic_test01 ( x_num, x, t ):

#*****************************************************************************80
#
## IC_TEST01 sets the initial condition for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real X(X_NUM), the node coordinates.
#
#    Input, real T, the time.
#
#    Output, real U(X_NUM), the initial value of U.
#
  import numpy as np

  u = np.zeros ( x_num )

  for i in range ( 0, x_num ):
    u[i] = 50.0

  return u

def k_test01 ( x_num, x, t ):

#*****************************************************************************80
#
## K_TEST01 evaluates the K coefficient for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of evaluation points.
#
#    Input, real X(X_NUM,1), the evaluation points.
#
#    Input, real T, the evaluation time.
#
#    Output, real K_VALUE(X_NUM,1), the value of K(X,T).
#
  import numpy as np

  k_value = np.zeros ( x_num )

  for i in range ( 0, x_num ):
    k_value[i] = 0.002

  return k_value

def rhs_test01 ( x_num, x, t ):

#*****************************************************************************80
#
## RHS_TEST01 evaluates the right hand side function for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of evaluation points.
#
#    Input, real X(X_NUM), the evaluation points.
#
#    Input, real T, the time.
#
#    Output, real RHS_VALUE(X_NUM), the right hand side function at
#    the given positions and time T.
#
  import numpy as np

  rhs_value = np.zeros ( x_num )

  return rhs_value

def fem1d_heat_explicit_test02 ( ):

#*****************************************************************************80
#
## FEM1D_HEAT_EXPLICIT_TEST02 does a problem with known solution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  from matplotlib.ticker import LinearLocator, FormatStrFormatter
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'FEM1D_HEAT_EXPLICIT_TEST02:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Using the finite element method,' )
  print ( '  compute an approximate solution to the time-dependent' )
  print ( '  one dimensional heat equation for a problem where we' )
  print ( '  know the exact solution.' )
  print ( '' )
  print ( '    dH/dt - K * d2H/dx2 = f(x,t)' )
#
#  Set the nodes.
#
  x_num = 21
  x_min = 0.0
  x_max = 1.0
  dx = ( x_max - x_min ) / ( x_num - 1 )
  x = np.linspace ( x_min, x_max, x_num )
#
#  Set the times.
#
  t_num = 51
  t_min = 0.0
  t_max = 10.0
  dt = ( t_max - t_min ) / ( t_num - 1 )
  t = np.linspace ( t_min, t_max, t_num )
#
#  Set finite element information.
#
  element_num = x_num - 1
  element_node = np.zeros ( [ 2, element_num ], dtype = np.int32 )
  for j in range ( 0, element_num ):
    element_node[0,j] = j
    element_node[1,j] = j + 1
  quad_num = 3
  mass = assemble_mass ( x_num, x, element_num, element_node, quad_num )

  print ( '' )
  print ( '  Number of X nodes = %d' % ( x_num ) )
  print ( '  X interval = [ %f, %f ]' % ( x_min, x_max ) )
  print ( '  X step size = %f' % ( dx ) )
  print ( '  Number of T steps = %d' % ( t_num ) )
  print ( '  T interval = [ %f, %f ]' % ( t_min, t_max ) )
  print ( '  T step size = %f' % ( dt ) )
  print ( '  Number of elements = %d' % ( element_num ) )
  print ( '  Number of quadrature points = %d' % ( quad_num ) )
#
#  Running the code produces an array H of temperatures H(t,x),
#  and vectors x and t.
#
  g_mat = np.zeros ( ( x_num, t_num ) )
  h_mat = np.zeros ( ( x_num, t_num ) )

  print ( '' )
  print ( '  Step            Time       RMS Error' )
  print ( '' )

  for j in range ( 0, t_num ):

    if ( j == 0 ):
      h = ic_test02 ( x_num, x, t[j] )
      h = bc_test02 ( x_num, x, t[j], h )
    else:
      h = fem1d_heat_explicit ( x_num, x, t[j-1], dt, k_test02, \
        rhs_test02, bc_test02, element_num, element_node, quad_num, mass, h )

    g = exact_test02 ( x_num, x, t[j] )
    e = 0.0
    for i in range ( 0, x_num ):
      e = e + ( h[i] - g[i] ) ** 2 
    e = np.sqrt ( e / x_num )
    print ( '  %4d  %14.6g  %14.6g' % ( j, t[j], e ) )

    for i in range ( 0, x_num ):
      g_mat[i,j] = g[i]
      h_mat[i,j] = h[i]
#
#  Make a product grid of T and X for plotting.
#
  t_mat, x_mat = np.meshgrid ( t, x )
#
#  Plot the data.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  surf = ax.plot_surface ( x_mat, t_mat, h_mat )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---T--->' )
  plt.title ( 'U(X,T)' )
  filename = 'plot_test02.png'
  plt.savefig ( filename )
  plt.show ( block = False )
#
#  Write the data to files.
#
  r8mat_write ( 'g_test02.txt', x_num, t_num, g_mat )
  r8mat_write ( 'h_test02.txt', x_num, t_num, h_mat )
  r8vec_write ( 't_test02.txt', t_num, t )
  r8vec_write ( 'x_test02.txt', x_num, x )

  print ( '' )
  print ( '  G(X,T) written to "g_test02.txt"' )
  print ( '  H(X,T) written to "h_test02.txt"' )
  print ( '  T values written to "t_test02.txt"' )
  print ( '  X values written to "x_test02.txt"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_HEAT_EXPLICIT_TEST02:' )
  print ( '  Normal end of execution.' )
  return

def bc_test02 ( x_num, x, t, h ):

#*****************************************************************************80
#
## BC_TEST02 evaluates the boundary conditions for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real X(X_NUM), the node coordinates.
#
#    Input, real T, the current time.
#
#    Input, real H(X_NUM), the current heat values.
#
#    Output, real H(X_NUM), the current heat values, after boundary
#    conditions have been imposed.
#
  import numpy as np

  x_array = np.zeros ( 1 )

  x_array[0] = x[0]
  h[0] = exact_test02 ( 1, x_array, t )

  x_array[0] = x[x_num-1]
  h[x_num-1] = exact_test02 ( 1, x_array, t )

  return h

def exact_test02 ( x_num, x, t ):

#*****************************************************************************80
#
## EXACT_TEST02 evaluates the exact solution for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real X(X_NUM), the node coordinates.
#
#    Input, real T, the initial time.
#
#    Output, real H(X_NUM), the exact solution at X and T.
#
  from math import exp
  from math import sin
  from math import sqrt
  import numpy as np

  k = k_test02 ( x_num, x, t )

  h = np.zeros ( x_num )

  for i in range ( 0, x_num ):
    h[i] = exp ( - t ) * sin ( sqrt ( k[i] ) * x[i] )

  return h

def ic_test02 ( x_num, x, t ):

#*****************************************************************************80
#
## IC_TEST02 evaluates the initial condition for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real X(X_NUM), the node coordinates.
#
#    Input, real T, the initial time.
#
#    Output, real H(X_NUM), the heat values at the initial time.
#
  h = exact_test02 ( x_num, x, t )

  return h

def k_test02 ( x_num, x, t ):

#*****************************************************************************80
#
## K_TEST02 evaluates the conductivity for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real K, the conducitivity.
#
#  Parameters:
#
#    Input, integer X_NUM, the number of evaluation points.
#
#    Input, real X(X_NUM), the evaluation points.
#
#    Input, real T, the evaluation time.
#
#    Output, real K_VALUE(X_NUM), the value of K(X,T).
#
  import numpy as np

  k_value = np.zeros ( x_num )

  for i in range ( 0, x_num ):
    k_value[i] = 0.002

  return k_value

def rhs_test02 ( x_num, x, t ):

#*****************************************************************************80
#
## RHS_TEST02 evaluates the right hand side for problem 2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real X(X_NUM), the node coordinates.
#
#    Input, real T, the time.
#
#    Output, real RHS_VALUE(X_NUM), the source term.
#
  import numpy as np

  rhs_value = np.zeros ( x_num )

  return rhs_value

def fem1d_heat_explicit_test03 ( ):

#*****************************************************************************80
#
## FEM1D_HEAT_EXPLICIT_TEST03 does a simple test problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  from matplotlib.ticker import LinearLocator, FormatStrFormatter
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'FEM1D_HEAT_EXPLICIT_TEST03:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Using the finite element method,' )
  print ( '  compute an approximate solution to the time-dependent' )
  print ( '  one dimensional heat equation:' )
  print ( '' )
  print ( '    dH/dt - K * d2H/dx2 = f(x,t)' )
#
#  Set the nodes.
#
  x_num = 21
  x_min = -5.0
  x_max = +5.0
  dx = ( x_max - x_min ) / ( x_num - 1 )
  x = np.linspace ( x_min, x_max, x_num )
#
#  Set the times.
#
  t_num = 321
  t_min = 0.0
  t_max = 4.0
  dt = ( t_max - t_min ) / ( t_num - 1 )
  t = np.linspace ( t_min, t_max, t_num )
#
#  Set finite element information.
#
  element_num = x_num - 1
  element_node = np.zeros ( [ 2, element_num ], dtype = np.int32 )
  for j in range ( 0, element_num ):
    element_node[0,j] = j
    element_node[1,j] = j + 1
  quad_num = 3
  mass = assemble_mass ( x_num, x, element_num, element_node, quad_num )

  print ( '' )
  print ( '  Number of X nodes = %d' % ( x_num ) )
  print ( '  X interval = [ %f, %f ]' % ( x_min, x_max ) )
  print ( '  X step size = %f' % ( dx ) )
  print ( '  Number of T steps = %d' % ( t_num ) )
  print ( '  T interval = [ %f, %f ]' % ( t_min, t_max ) )
  print ( '  T step size = %f' % ( dt ) )
  print ( '  Number of elements = %d' % ( element_num ) )
  print ( '  Number of quadrature points = %d' % ( quad_num ) )
#
#  Running the code produces an array H of temperatures H(t,x),
#  and vectors x and t.
#
  h_mat = np.zeros ( ( x_num, t_num ) )

  for j in range ( 0, t_num ):

    if ( j == 0 ):
      h = ic_test03 ( x_num, x, t[j] )
      h = bc_test03 ( x_num, x, t[j], h )
    else:
      h = fem1d_heat_explicit ( x_num, x, t[j-1], dt, k_test03, \
        rhs_test03, bc_test03, element_num, element_node, quad_num, mass, h )

    for i in range ( 0, x_num ):
      h_mat[i,j] = h[i]

  t_mat, x_mat = np.meshgrid ( t, x )
#
#  Make a mesh plot of the solution.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  surf = ax.plot_surface ( x_mat, t_mat, h_mat )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---T--->' )
  plt.title ( 'U(X,T)' )
  filename = 'plot_test03.png'
  plt.savefig ( filename )
  plt.show ( block = False )
#
#  Write the data to files.
#
  r8mat_write ( 'h_test03.txt', x_num, t_num, h_mat )
  r8vec_write ( 't_test03.txt', t_num, t )
  r8vec_write ( 'x_test03.txt', x_num, x )

  print ( '' )
  print ( '  H(X,T) written to "h_test03.txt"' )
  print ( '  T values written to "t_test03.txt"' )
  print ( '  X values written to "x_test3.txt"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_HEAT_EXPLICIT_TEST03:' )
  print ( '  Normal end of execution.' )
  return

def bc_test03 ( x_num, x, t, h ):

#*****************************************************************************80
#
## BC_TEST03 evaluates the boundary conditions for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real X(X_NUM,1), the node coordinates.
#
#    Input, real T, the current time.
#
#    Input, real H(X_NUM), the current heat values.
#
#    Output, real H(X_NUM), the current heat values, after boundary
#    conditions have been imposed.
#
  h[0]       = 15.0
  h[x_num-1] = 25.0

  return h

def ic_test03 ( x_num, x, t ):

#*****************************************************************************80
#
## IC_TEST03 evaluates the initial condition for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real X(X_NUM,1), the node coordinates.
#
#    Input, real T, the initial time.
#
#    Output, real H(X_NUM,1), the heat values at the initial time.
#
  import numpy as np

  h = np.zeros ( x_num )

  for i in range ( 0, x_num ):
    if ( x[i] < 0.0 ):
      h[i] = 15.0
    elif ( x[i] == 0.0 ):
      h[i] = 20.0
    else:
      h[i] = 25.0

  return h

def k_test03 ( x_num, x, t ):

#*****************************************************************************80
#
## K_TEST03 evaluates the conductivity for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of evaluation points.
#
#    Input, real X(X_NUM,1), the evaluation points.
#
#    Input, real T, the evaluation time.
#
#    Output, real K_VALUE(X_NUM,1), the value of K(X,T).
#
  import numpy as np

  k_value = np.zeros ( x_num )

  for i in range ( 0, x_num ):
    k_value[i] = 2.0

  return k_value

def rhs_test03 ( x_num, x, t ):

#*****************************************************************************80
#
## RHS_TEST03 evaluates the right hand side for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real X(X_NUM,1), the node coordinates.
#
#    Input, real T, the current time.
#
#    Output, real RHS_VALUE(X_NUM,1), the source term.
#
  import numpy as np

  rhs_value = np.zeros ( x_num )

  return rhs_value

def fem1d_heat_explicit_test ( ):

#*****************************************************************************80
#
## FEM1D_HEAT_EXPLICIT_TEST tests the FEM1D_HEAT_EXPLICIT library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'FEM1D_HEAT_EXPLICIT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the FEM1D_HEAT_EXPLICIT library.' )

  fem1d_heat_explicit_test01 ( )
  fem1d_heat_explicit_test02 ( )
  fem1d_heat_explicit_test03 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_HEAT_EXPLICIT_TEST' )
  print ( '  Normal end of execution.' )
  return

def quadrature_set ( quad_num ):

#*****************************************************************************80
#
## QUADRATURE_SET sets abscissas and weights for Gauss-Legendre quadrature.
#
#  Discussion:
#
#    The integration interval is [ -1, 1 ].
#
#    The weight function w(x) = 1.0
#
#    The integral to approximate:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    Quadrature rule:
#
#      Sum ( 1 <= I <= QUAD_NUM ) QUAD_W(I) * F ( QUAD_X(I) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer QUAD_NUM, the order of the rule.
#    QUAD_NUM must be between 1 and 6.
#
#    Output, real QUAD_W(QUAD_NUM), the weights of the rule.
#
#    Output, real QUAD_X(QUAD_NUM), the abscissas of the rule.
#
  from sys import exit
  import numpy as np

  if ( quad_num == 1 ):

    quad_x = np.array ( [ \
      0.0 ] )

    quad_w = np.array ( [ \
      2.0 ] )

  elif ( quad_num == 2 ):

    quad_x = np.array ( [ \
      - 0.577350269189625764509148780502, \
        0.577350269189625764509148780502 ] )

    quad_w = np.array ( [ \
      1.0, \
      1.0 ] )

  elif ( quad_num == 3 ):

    quad_x = np.array ( [ \
      - 0.774596669241483377035853079956, \
        0.0, \
        0.774596669241483377035853079956 ] )

    quad_w = np.array ( [ \
      5.0 / 9.0, \
      8.0 / 9.0, \
      5.0 / 9.0 ] )

  elif ( quad_num == 4 ):

    quad_x = np.array ( [ \
      - 0.861136311594052575223946488893, \
      - 0.339981043584856264802665759103, \
        0.339981043584856264802665759103, \
        0.861136311594052575223946488893 ] )

    quad_w = np.array ( [ \
      0.347854845137453857373063949222, \
      0.652145154862546142626936050778, \
      0.652145154862546142626936050778, \
      0.347854845137453857373063949222 ] )

  elif ( quad_num == 5 ):

    quad_x = np.array ( [ \
      - 0.906179845938663992797626878299, \
      - 0.538469310105683091036314420700, \
        0.0, \
        0.538469310105683091036314420700, \
        0.906179845938663992797626878299 ] )

    quad_w = np.array ( [ \
      0.236926885056189087514264040720, \
      0.478628670499366468041291514836, \
      0.568888888888888888888888888889, \
      0.478628670499366468041291514836, \
      0.236926885056189087514264040720 ] )

  elif ( quad_num == 6 ):
    quad_x = np.array ( [ \
      - 0.932469514203152027812301554494, \
      - 0.661209386466264513661399595020, \
      - 0.238619186083196908630501721681, \
        0.238619186083196908630501721681, \
        0.661209386466264513661399595020, \
        0.932469514203152027812301554494 ] )

    quad_w = np.array ( [ \
      0.171324492379170345040296142173, \
      0.360761573048138607569833513838, \
      0.467913934572691047389870343990, \
      0.467913934572691047389870343990, \
      0.360761573048138607569833513838, \
      0.171324492379170345040296142173 ] )

  else:

    print ( '' )
    print ( 'QUADRATURE_SET - Fatal error!' )
    print ( '  The requested order %d is not available.' % ( quad_num ) )
    exit ( 'QUADRATURE_SET - Fatal error!' )

  return quad_w, quad_x

def quadrature_set_test ( ):

#*****************************************************************************80
#
## QUADRATURE_SET_TEST tests QUADRATURE_SET.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'QUADRATURE_SET_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  QUADRATURE_SET returns points and weights for a quadrature rule.' )

  quad_num = 4
  quad_w, quad_x = quadrature_set ( quad_num )

  print ( '' )
  print ( '   I      W[i]    X[i]' )
  print ( '' )
  for i in range ( 0, quad_num ):
    print ( '  %2d  %8.4f  %8.4f' % ( i, quad_w[i], quad_x[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'QUADRATURE_SET_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_write ( filename, m, n, a ):

#*****************************************************************************80
#
## R8MAT_WRITE writes an R8MAT to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the output file.
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      s = '  %g' % ( a[i,j] )
      output.write ( s )
    output.write ( '\n' )

  output.close ( )

  return

def r8mat_write_test ( ):

#*****************************************************************************80
#
## R8MAT_WRITE_TEST tests R8MAT_WRITE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_WRITE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test R8MAT_WRITE, which writes an R8MAT to a file.' )

  filename = 'r8mat_write_test.txt'
  m = 5
  n = 3
  a = np.array ( (  \
    ( 1.1, 1.2, 1.3 ), \
    ( 2.1, 2.2, 2.3 ), \
    ( 3.1, 3.2, 3.3 ), \
    ( 4.1, 4.2, 4.3 ), \
    ( 5.1, 5.2, 5.3 ) ) )
  r8mat_write ( filename, m, n, a )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_WRITE_TEST:' )
  print ( '  Normal end of execution.' )
  return
  
def r8vec_write ( filename, n, a ):

#*****************************************************************************80
#
## R8VEC_WRITE writes an R8VEC to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the output file.
#
#    Input, integer N, the number of entries in A.
#
#    Input, real A(N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, n ):
    s = '  %g\n' % ( a[i] )
    output.write ( s )

  output.close ( )

  return

def r8vec_write_test ( ):

#*****************************************************************************80
#
## R8VEC_WRITE_TEST tests R8VEC_WRITE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_WRITE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test R8VEC_WRITE, which writes an R8VEC to a file.' )
  filename = 'r8vec_write_test.txt'
  n = 5
  a = np.array ( ( 1.1, 2.2, 3.3, 4.4, 5.5 ) )
  r8vec_write ( filename, n, a )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_WRITE_TEST:' )
  print ( '  Normal end of execution.' )
  return
  
def reference_to_physical ( element, element_node, node_x, reference_num, \
  reference_x ):

#*****************************************************************************80
#
## REFERENCE_TO_PHYSICAL maps points in the reference interval into an element.
#
#  Discussion:
#
#    The reference interval is [ -1.0, +1.0 ].
#
#    Element ELEMENT extends from node ELEMENT_NODE(1,ELEMENT) to 
#    ELEMENT_NODE(2,ELEMENT).
#
#    The coordinate of node NODE is NODE_X(NODE).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ELEMENT, the index of the element.
#
#    Input, integer ELEMENT_NODE(ELEMENT_ORDER,ELEMENT_NUM);
#    ELEMENT_NODE(I,J) is the global index of local node I in element J.
#
#    Input, real NODE_X(NODE_NUM), the coordinates of nodes.
#
#    Input, integer REFERENCE_NUM, the number of points in the reference
#    interval to be transformed.
#
#    Input, real REFERENCE_X(REFERENCE_NUM), the coordinates of the
#    points in the reference interval.
#
#    Output, real PHYSICAL_X(REFERENCE_NUM), the coordinates of the
#    points in the element which correspond to the reference points.
#
  import numpy as np

  physical_x = np.zeros ( reference_num )

  for i in range ( 0, reference_num ):
    a = node_x[element_node[0,element] ]
    b = node_x[element_node[1,element] ]

    physical_x[i] = ( ( 1.0 - reference_x[i]             ) * a   \
                    + (       reference_x[i] - ( - 1.0 ) ) * b ) \
                    / ( 1.0                  - ( - 1.0 ) )

  return physical_x

def reference_to_physical_test ( ):

#*****************************************************************************80
#
## REFERENCE_TO_PHYSICAL_TEST tests REFERENCE_TO_PHYSICAL
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'REFERENCE_TO_PHYSICAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  REFERENCE_TO_PHYSICAL maps points in [-1,+1] to points in' )
  print ( '  a physical interval.' )

  element_num = 4
  element_node = np.array ( [ [ 0, 1, 2, 3 ], [ 1, 2, 3, 4 ] ] )

  node_num = 5
  node_x = np.array ( [ 0.0, 2.0, 3.0, 6.0, 10.0 ] )

  reference_num = 5
  reference_x = np.array ( [ -1.0, -0.5, 0.0, 0.25, 1.0 ] )

  element = 3
  physical_x = reference_to_physical ( element, element_node, node_x, \
    reference_num, reference_x )

  print ( '' )
  print ( '   I      Ref[i]    Phys[i]' )
  print ( '' )
  for i in range ( 0, reference_num ):
    print ( '  %2d  %8.4f  %8.4f' % ( i, reference_x[i], physical_x[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'REFERENCE_TO_PHYSICAL_TEST:' )
  print ( '  Normal end of execution.' )
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
  fem1d_heat_explicit_test ( )
  timestamp ( )

