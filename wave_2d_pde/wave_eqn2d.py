import numpy as np

class WaveEqn2D:

  def __init__( self, nx=500, ny=500, c=0.2, h=1, dt=1,
    use_mur_abc=True ):
    """Initialize the simulation:
    nx and ny are the dimension of the domain;
    c is the wave speed;
    h and dt are the space and time grid spacings;
    If use_mur_abc is True, the Mur absorbing boundary
    conditions will be used; if False, the Dirichlet
    (reflecting) boundary conditions are used.
    """
    self.nx = nx
    self.ny = ny
    self.c = c
    self.h = 1
    self.dt = 1
    self.use_mur_abc = use_mur_abc
    self.alpha = self.c * self.dt / self.h
    self.alpha2 = self.alpha**2
    self.u = np.zeros( (3, ny, nx) )

  def update ( self ):
    """Update the simulation by one time tick."""
# The three planes of u correspond to the time points
# k+1, k and k-1; i.e. we calculate the next frame
# of the simulation (k+1) in u[0,...].
    u, nx, ny = self.u, self.nx, self.ny
    u[2] = u[1] # old k -> new k-1
    u[1] = u[0] # old k+1 -> new k
#
# Calculate the new k+1:
#
    u[0, 1:ny-1, 1:nx-1] = self.alpha2 * (
      u[1, 0:ny-2, 1:nx-1]
      + u[1, 2:ny,1:nx-1]
      + u[1, 1:ny-1, 0:nx-2]
      + u[1, 1:ny-1, 2:nx]
      - 4*u[1, 1:ny-1, 1:nx-1]) \
      + (2 * u[1, 1:ny-1, 1:nx-1]
      - u[2, 1:ny-1, 1:nx-1])

    if self.use_mur_abc:
# Mur absorbing boundary conditions.
      kappa = (1 - self.alpha) / (1 + self.alpha)
      u[0, 0, 1:nx-1] = ( u[1, 1, 1:nx-1]
        - kappa * (
        u[0, 1, 1:nx-1]
        - u[1, 0, 1:nx-1])
        )
      u[0, ny-1, 1:nx-1] = (u[1, ny-2, 1:nx-1]
        + kappa * (
        u[1, ny-1, 1:nx-1]
        - u[0, ny-2, 1:nx-1])
        )
      u[0, 1:ny-1, 0] = (u[1, 1:ny-1, 1]
        - kappa * (
        u[0, 1:ny-1, 1]
        - u[1, 1:ny-1, 0])
        )
      u[0, 1:ny-1, nx-1] = (u[1, 1:ny-1, nx-2]
        + kappa * (
        u[1, 1:ny-1, nx-1]
        - u[0, 1:ny-1, nx-2])
        )
