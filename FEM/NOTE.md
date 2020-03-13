# FEM

## fd1d_advection_lax_wendroff.py

Finite Difference Method, 1D Advection Equation, Lax-Wendroff Method

```markdown
du/dt = - c du/dx
0.0 <= x <= 1.0

u(0,x) = (10x-4)^2 (6-10x)^2 for 0.4 <= x <= 0.6
       = 0 elsewhere.
```

## fd1d_bvp.py

## fd1d_heat_explicit.py

## fd1d_heat_implicit.py

## fd2d_heat_steady.py

## fd_predator_prey

Finite Difference Solution of a Predator Prey ODE System

finite difference method
to estimate solutions of a pair of ordinary differential equations
that model the behavior of a pair of predator and prey populations.

The PREY reproduce rapidly;  
for each animal alive at the beginning of the year, two more will be born by the end of the year.  
The prey do not have a natural death rate; instead, they only die by being eaten by the predator.  
Every prey animal has 1 chance in 1000 of being eaten in a given year by a given predator.

The PREDATORS only die of starvation, but this happens very quickly.  
If unfed, a predator will tend to starve in about 1/10 of a year.  
On the other hand, the predator reproduction rate is dependent on eating prey,
and the chances of this depend on the number of available prey.

```markdown
PREY(0) = 5000
PRED(0) =  100

d PREY / dT =    2 * PREY(T) - 0.001 * PREY(T) * PRED(T)
d PRED / dT = - 10 * PRED(T) + 0.002 * PREY(T) * PRED(T)
d PREY / dT = approximately ( PREY(T+DT) - PREY(T) ) / DT
PREY(T+DT) = PREY(T) + DT * ( 2 * PREY(T) - 0.001 * PREY(T) * PRED(T) ).
```

## fem1d.py

## fem1d_bvp_linear.py

## fem1d_bvp_quadratic.py

## fem1d_classes.py

## fem1d_classes_test.py

## fem1d_heat_explicit.py

## fem1d_model.py

## fem2d_bvp_linear.py

FEM2D_BVP_LINEAR solves a 2D boundary value problem in the unit square.

the PDE is defined for 0 < x < 1, 0 < y < 1:

- uxx - uyy = f(x)

```markdown
with boundary conditions
  u(0,y) = 0,
  u(1,y) = 0,
  u(x,0) = 0,
  u(x,1) = 0.

The exact solution is:
  exact(x) = x * ( 1 - x ) * y * ( 1 - y ).

The right hand side f(x) is:
  f(x) = 2 * x * ( 1 - x ) + 2 * y * ( 1 - y )
```

The unit square is divided into N by N squares.  Bilinear finite
element basis functions are defined, and the solution is sought as
piecewise linear combination of these basis functions.

## fem_basis

- test01 - FEM_BASIS_1D
  - fem_basis_1d
- test02 - FEM_BASIS_2D
  - fem_basis_2d
- test03 - FEM_BASIS_3D
  - fem_basis_3d
- test04 - FEM_BASIS_MD
  - fem_basis_md
  - basis function over an M-dimensional simplex
  - m = 1
- test05 - FEM_BASIS_MD
  - fem_basis_md
  - basis function over an M-dimensional simplex
  - m = 2
- test06 - FEM_BASIS_MD
  - fem_basis_md
  - basis function over an M-dimensional simplex
  - m = 3
- test07 - FEM_BASIS_PRISM_TRIANGLE
  - fem_basis_prism_triangle
  - basis function over a right triangular prism
  - up to degree 2 in X and Y, and up to degree 2 in Z
- test08 - FEM_BASIS_PRISM_TRIANGLE
  - fem_basis_prism_triangle
  - basis function over a right triangular prism
  - up to degree 3 in X and Y, and up to degree 1 in Z

## fem_basis_test01.py

## fem_to_xml.py

## xml_to_fem.py
