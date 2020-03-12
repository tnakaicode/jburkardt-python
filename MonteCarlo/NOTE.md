# Monte Carlo

## annulus_monte_carlo

Monte Carlo Estimate of Integrals in an Annulus

Monte Carlo method to estimate the integral of a function over the interior of a circular annulus in 2D.

A circular annulus with center (XC,YC), inner radius R1 and outer radius R2, is the set of points (X,Y) so that
$$ R_1^2 <= (x-x_c)^2 + (y-y_c)^2 <= R_2^2  $$

```Python
e = [0, 2]
value = monomial_value(2, n, e, x)
result = annulus_area(center, r1, r2) * np.sum(value[:]) / n
```

## ball_monte_carlo

Monte Carlo method to estimate integrals of a function over the interior of the unit ball in 3D

## circle_monte_carlo

Monte Carlo method to estimate the integral of a function on the circumference of the unit circle in 2D;

## cube_monte_carlo

Monte Carlo method to estimate the integral of a function over the interior of the unit cube in 3D.

## disk01_monte_carlo

Monte Carlo method to estimate integrals over the interior of the unit disk in 2D.

## disk01_quarter_monte_carlo

Monte Carlo method to estimate the integral of a function over the interior of the unit quarter disk in 2D;

## disk_monte_carlo

Monte Carlo method to estimate integrals over the interior of a disk in 2D.

## ellipse_monte_carlo

Monte Carlo method to estimate the value of integrals over the interior of an ellipse in 2D.

## ellipsoid_monte_carlo

Monte Carlo method to estimate the value of integrals over the interior of an ellipsoid in M dimensions.

## hyperball_monte_carlo

Monte Carlo method to estimate the integral of a function over the interior of the unit hyperball in M dimensions;

## hypercube_monte_carlo

Monte Carlo method to estimate the integral of a function over the interior of the unit hypercube in M dimensions.

## hypersphere_monte_carlo

Monte Carlo method to estimate the integral of a function on the surface of the unit sphere in M dimensions;

## line_monte_carlo

Monte Carlo method to estimate integrals over the length of the unit line in 1D.

## polygon_monte_carlo

Monte Carlo method to estimate the integral of a function over the interior of a polygon in 2D.

## pyramid_monte_carlo

Monte Carlo method to estimate integrals of a function over the interior of the unit pyramid in 3D;

## simplex_monte_carlo

Monte Carlo method to estimate integrals over the interior of the unit simplex in M dimensions.

## sphere_monte_carlo

Monte Carlo method to estimate integrals of a function over the surface of the unit sphere in 3D;

## square_monte_carlo

Monte Carlo method to estimate the integral of a function over the interior of the unit square in 2D.

## tetrahedron01_monte_carlo

Monte Carlo method to estimate integrals over a tetrahedron.

## triangle01_monte_carlo

Monte Carlo method to estimate integrals over the interior of the unit triangle in 2D.

## triangle_monte_carlo.py

## wedge_monte_carlo.py

Monte Carlo method to estimate integrals over the interior of the unit wedge in 3D.
