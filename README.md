# jburkardt-python

get python code

```bash
wget -r -np -l 0 http://people.sc.fsu.edu/~jburkardt/py_src/
wget -r -np -l 0 http://people.sc.fsu.edu/~jburkardt/fenics_src/
wget -r -np -l 0 http://people.sc.fsu.edu/~jburkardt/data/

http://ossanworld.com/cfdbooks/cfdcodes.html
```

## Interpolate

- barycentric_interp_1d
- chebyshev_interp_1d
- lagrange_interp_1d
- nearest_interp_1d
- newton_interp_1d
- pwl_interp_1d
- pwl_interp_2d
- rbf_interp_1d
- rbf_interp_2d
- shepard_interp_1d
- test_interp
- test_interp_1d
- test_interp_2d
- triangle_interpolate
- vandermonde_interp_1d

## Monte Calro

- annulus_monte_carlo
- ball_monte_carlo
- circle_monte_carlo
- cube_monte_carlo
- disk01_monte_carlo
- disk01_quarter_monte_carlo
- disk_monte_carlo
- ellipse_monte_carlo
- ellipsoid_monte_carlo
- hyperball_monte_carlo
- hypercube_monte_carlo
- hypersphere_monte_carlo
- line_monte_carlo
- polygon_monte_carlo
- pyramid_monte_carlo
- simplex_monte_carlo
- sphere_monte_carlo
- square_monte_carlo
- tetrahedron01_monte_carlo
- triangle01_monte_carlo
- triangle_monte_carlo
- wedge_monte_carlo

## Integral

- ball_integrals
- circle_integrals
- cube_integrals
- disk01_integrals
- elliptic_integral
- hyperball_integrals
- hypercube_integrals
- hypersphere_integrals
- line_integrals
- polygon_integrals
- pyramid_integrals
- simplex_integrals
- sphere_integrals
- square_integrals
- tetrahedron_integrals
- triangle01_integrals
- triangle_integrals
- wedge_integrals

## Probability Density Functions

prob

For a discrete variable X, PDF(X) is the probability that the value X will occur  
for a continuous variable, PDF(X) is the probability density of X,  
the probability of a value between $X$ and $X+dX$ is $PDF(X) * dX$

CDF - Cumulative Density Functions  

- cardioid
  - cardioid_cdf_test
  - cardioid_sample_test
  - cardioid_cdf
  - cardioid_cdf_inv
  - cardioid_pdf

$$ pdf(A, Bx) = \frac{1}{2 \pi} (1 + 2B \cos(X-A)) $$

## Grid

- ball_grid
- circle_arc_grid
- cube_grid
- disk_grid
- ellipse_grid
- ellipsoid_grid
- grid
- hypercube_grid
- line_grid
- polygon_grid
- pyramid_grid
- simplex_grid
- sphere_fibonacci_grid
- sphere_llq_grid
- sphere_llt_grid
- square_grid
- tetrahedron_grid
- triangle_grid
- wedge_grid

## toms

- toms097
  - All Pairs Shortest Distance, Floyd's Algorithm.
- toms112
  - determines whether a point is inside a polygon.
- toms178
  - Minimization by Hooke-Jeeves Direct Search
- toms179
  - Modified Beta Function
- toms243
  - evaluates the logarithm of a complex value, by David Collens.
- toms515
  - subsets of an N set
- toms577
  - Carlson's Elliptic Integrals
  - functions RC, RD, RF and RJ.
- toms655
  - Weights for Interpolatory Quadrature
- toms743
  - Evaluation of Lambert's W function.

## toms743 Lambert's W function

omega function or product logarithm
the branches of the inverse relation of function $f(w)=w e^w$, where w is complex

for each integer k there is one branch, $$W_0$$ is principle branch.

$w e^w = z$

$$ W_0 (x) = \Sigma_{n=1}^{\infin} \frac{(-1)^{n-1}}{n!} x^n $$
