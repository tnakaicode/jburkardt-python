# Quadrule

## bashforth

Adams-Bashforth quadrature formulas
solving ordinary differential equations
not really suitable for general quadrature computations

to approximating the integral of F(Y(X)) between X(M) and X(M+1)
relies only on known values of F(Y(X)) at X(M-N+1) through X(M).

the unknown function is denoted by Y(X), with derivative F(Y(X))
approximate values of the function are known at a series of X values

X(1), X(2), ..., X(M)
Y(X(1)) as Y(1)

Y(M+1) = Y(M) + Integral ( X(M) < X < X(M+1) ) F(Y(X)) dX
       = Y(M) + H * Sum ( 1 <= I <= N ) W(I) * F(Y(M+1-I))
approximately.

## chebyshev

integral ( -1 <= x <= +1 ) x^n / sqrt(1-x^2) dx

## NC_Compute

Newton-Cotes qudrature rule estimate

Integral (X_MIN <= X <= X_MAX ) F(X) dX

Sum ( 1 <= I <= N ) W(I)*F(X(I))

## Radau Rule
