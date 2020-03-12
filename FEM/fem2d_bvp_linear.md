# fem2d_bvp_linear

FEM2D_BVP_LINEAR solves a 2D boundary value problem in the unit square.

the PDE is defined for 0 < x < 1, 0 < y < 1:

- uxx - uyy = f(x)

with boundary conditions
  u(0,y) = 0,
  u(1,y) = 0,
  u(x,0) = 0,
  u(x,1) = 0.

The exact solution is:
  exact(x) = x * ( 1 - x ) * y * ( 1 - y ).

The right hand side f(x) is:
  f(x) = 2 * x * ( 1 - x ) + 2 * y * ( 1 - y )

The unit square is divided into N by N squares.  Bilinear finite
element basis functions are defined, and the solution is sought as 
piecewise linear combination of these basis functions.
