---
title: Exact Solution of Time Dependent 1D Viscous Burgers Equation
---

## burgers_viscous_time_exact1

    The form of the Burgers equation considered here is

      du       du        d^2 u
      -- + u * -- = nu * -----
      dt       dx        dx^2

    for -1.0 < x < +1.0, and 0 < t.

    Initial conditions are 
    
        u(x,0) = - sin(pi*x).  
    
    Boundary conditions are 

        u(-1,t) = u(+1,t) = 0.  
    
    The viscosity parameter nu is taken to be 0.01 / pi, 
    although this is not essential.

    The authors note an integral representation for 
        the solution u(x,t),
    and present a better version of the formula 
        that is amenable to approximation 
        using Hermite quadrature.

    This program library does little more than 
        evaluate the exact solution at a user-specified set of points, 
        using the quadrature rule.
    Internally, the order of this quadrature rule 
        is set to 8, 
        but the user can easily modify this value 
    if greater accuracy is desired.

## burgers_viscous_time_exact2

    The form of the Burgers equation considered here is

      du       du        d^2 u
      -- + u * -- = nu * -----
      dt       dx        dx^2

    for 0.0 < x < 2 Pi, and 0 < t.

    The initial condition is

      u(x,0) = 4 - 2 * nu * dphi(x,0)/dx / phi(x,0)

    where

      phi(x,t) = exp ( - ( x-4*t      ) / ( 4*nu*(t+1) ) )
               + exp ( - ( x-4*t-2*pi ) / ( 4*nu*(t+1) ) )

    The boundary conditions are periodic:

      u(0,t) = u(2 Pi,t)

    The viscosity parameter nu may be taken 
        to be 0.01, 
        but other values may be chosen.
