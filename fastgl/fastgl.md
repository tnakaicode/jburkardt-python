# fastgl

- besseljzero_test
  - SCIPY.SPECIAL provides the built in J0(X) function.
  - Iteration-free computation of Gauss-Legendre quadrature nodes and weights,
- besselj1squared_test
  - SCIPY.SPECIAL provides the built in function J1.
- glpair_test
  - the numerical integration of ln(x) over the range [0,1]
  - one would not use Gauss-Legendre quadrature for this
- glpairs_test
  - the numerical integration of cos(1000 x) over the range [-1,1]
  - for varying number of Gauss-Legendre quadrature nodes l.
- glpairtabulated_test
- legendre_theta_test
- legendre_weight_test
