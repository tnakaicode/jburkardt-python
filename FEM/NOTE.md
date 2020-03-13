# FEM

## fd1d_advection_lax_wendroff.py

Finite Difference Method, 1D Advection Equation, Lax-Wendroff Method

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

## fem_basis.py

## fem_basis_test01.py

## fem_to_xml.py

## xml_to_fem.py
