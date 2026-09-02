#! /usr/bin/env python3
#
from matplotlib.colors import TwoSlopeNorm
import argparse
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import platform

# ── Grid ──────────────────────────────────────────────────────────────────────
Nx, Ny = 400, 400

# ── D2Q9 constants ────────────────────────────────────────────────────────────
EIX = np.array ( [ 0,  1,  0, -1,  0,  1, -1, -1,  1], dtype=float )
EIY = np.array ( [ 0,  0,  1,  0, -1,  1,  1, -1, -1], dtype=float )
OPP = np.array ( [ 0,  3,  4,  1,  2,  7,  8,  5,  6], dtype=int )
W   = np.array ( [4/9, 1/9, 1/9, 1/9, 1/9, 1/36, 1/36, 1/36, 1/36] )

cs2 = 1.0 / 3.0   # lattice speed of sound squared

# ── Physical parameters ───────────────────────────────────────────────────────
rho0 = 1.0
uw   = 0.1
R    = Ny // 10

def main ( ):

#*****************************************************************************80
#
## lbm() demonstrates the Lattice Boltzmann Method.
#
#  Discussion:
#
#    The local cell is divided into 9 subcells, labeled as follows:
#
#      6  2  5
#      3  0  1
#      7  4  8
#
#  Modified:
#
#    05 August 2026
#
#  Reference:
#
#    Ferran Alia
#    This version by John Burkardt
#
#  Reference:
#
#    Ferran Alia,
#    The fluid simulator that doesn't solve the fluid equations,
#    Towards Data Science,
#    25 July 2026.
#
  print ( '' )
  print ( 'lbm():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  lbm() demonstrates the Lattice Boltzmann Method.' )

  parser = argparse.ArgumentParser(
        description='LBM fluid solver (NumPy reference implementation)'
    )
  parser.add_argument('--tau',       type=float, default=0.55,
                        help='Relaxation time. Controls viscosity: nu=cs2*(tau-0.5). '
                             'Use 0.55 for Karman vortex street, 0.75 for laminar wake. '
                             'Must be > 0.5 for stability.')
  parser.add_argument('--steps',     type=int,   default=5000,
                        help='Total number of timesteps.')
  parser.add_argument('--out_every', type=int,   default=500,
                        help='Save/show a plot every N steps.')
  parser.add_argument('--save_dir',  type=str,   default='lbm_output',
                        help='Directory for output images. '
                             'Set to empty string to display plots interactively.')
  args = parser.parse_args()

  tau = args.tau
  steps = args.steps

  nu = cs2 * ( tau - 0.5 )
  Re = uw * ( 2 * R ) / nu

  print ( '  Grid: ', Nx, 'x', Ny )
  print (f"tau       : {tau:.3f}  =>  nu = {nu:.4f}  =>  Re = {Re:.1f}")
  print (f"Steps     : {steps}")
  print (f"Output    : every {args.out_every} steps -> '{args.save_dir or 'interactive'}'")
  print ()
#
#  Define the obstacle.
#
  solid = make_solid_cylinder ( cx = Nx//4, cy = Ny//2 + 5, r = R )
#
#  Initialize f().
#
  f = initialize ( solid )

  for step in range ( steps ):
#
#  Compute density and velocity from f().
#
    rho, ux, uy = macros ( f, solid )
#
#  Relax each f toward f^eq at rate 1/tau.
#
    f = collide ( f, rho, ux, uy, solid, tau )
    f_before = f.copy()
#
#  Propagate each population to the neighboring node.
#
    f = stream ( f )
    f = apply_bounce_back ( f, f_before, solid )
    f = apply_boundaries ( f )
#
#  Dump plot information every so often.
#
    if ( step % args.out_every == 0 ):
      print ( f'Step {step:>6d} / {steps}' )
      save_dir = args.save_dir if args.save_dir else None
      plot_state ( rho, ux, uy, solid, step, save_dir = save_dir )
#
#  Final frame
#
  rho, ux, uy = macros ( f, solid )

  plot_state ( rho, ux, uy, solid, steps,
               save_dir=args.save_dir if args.save_dir else None)

  print('Done.')

def apply_bounce_back ( f, f_before, solid ):

#*****************************************************************************80
#
## apply_bounce_back() handles no-slip walls.
#
#  Discussion:
#
#    Local particles that would have been sent to the solid are instead
#    "bounced back".
#
#  Modified:
#
#    01 August 2026
#
#  Reference:
#
#    Ferran Alia
#    This version by John Burkardt
#
  f_out = f.copy()

  for i in range(9):
    f_out[i, solid] = f_before[OPP[i], solid]

  return f_out

def apply_boundaries ( f ):

#*****************************************************************************80
#
## apply_boundaries() applies boundary conditions.
#
#  Modified:
#
#    01 August 2026
#
#  Reference:
#
#    Ferran Alia
#    This version by John Burkardt
#

#
#  Fixed velocity uw at the inlet.
#
  ux_in = uw

  rho_in = (
      ( 1.0 / ( 1.0 - ux_in ) ) *
      ( f[0, 0, :] + f[2, 0, :] + f[4, 0, :]
       + 2.0 * (f[3, 0, :] + f[6, 0, :] + f[7, 0, :]) )
  )
#
#  Reconstruct 3 missing rightward-pointing populations.
#
  f[1, 0, :] = f[3, 0, :] \
    + ( 2.0 / 3.0 ) * rho_in * ux_in

  f[5, 0, :] = f[7, 0, :] - 0.5*(f[2, 0, :] - f[4, 0, :]) \
    + ( 1.0 / 6.0 ) * rho_in * ux_in

  f[8, 0, :] = f[6, 0, :] + 0.5*(f[2, 0, :] - f[4, 0, :]) \
    + ( 1.0 / 6.0 ) * rho_in * ux_in
#
#  Zero-gradient outlet at x=Nx-1
#
  f[:, Nx-1, :] = f[:, Nx-2, :]

  return f

def collide ( f, rho, ux, uy, solid, tau ):

#*****************************************************************************80
#
## collide() relaxes each f toward f^eq at rate 1/tau.
#
#  Modified:
#
#    31 July 2026
#
#  Reference:
#
#    Ferran Alia
#    This version by John Burkardt
#
  feq = equilibrium ( rho, ux, uy )
  f_out = f - ( 1.0 / tau ) * ( f - feq )
  f_out[:, solid] = f[:, solid]

  return f_out

def equilibrium ( rho, ux, uy ):

#*****************************************************************************80
#
## equilibrium() computes the equilibrium value of f.
#
#  Modified:
#
#    01 August 2026
#
#  Reference:
#
#    Ferran Alia
#    This version by John Burkardt
#
  u2 = ux**2 + uy**2

  eu = EIX[:, None, None] * ux \
     + EIY[:, None, None] * uy

  feq = W[:, None, None] * rho * (
      1.0  +  eu / cs2
           +  eu**2 / ( 2.0 * cs2**2 )
           -  u2    / ( 2.0 * cs2 )
  )
  return feq

def initialize ( solid ):

#*****************************************************************************80
#
## initialize() initializes the f field.
#
#  Modified:
#
#    01 August 2026
#
#  Reference:
#
#    Ferran Alia
#    This version by John Burkardt
#
  rho = np.ones( (Nx, Ny) ) * rho0

  ux  = np.ones( (Nx, Ny) ) * uw
  uy  = np.zeros( (Nx, Ny) )

  f = equilibrium ( rho, ux, uy )
  f = f + ( np.random.rand ( 9, Nx, Ny ) - 0.5 ) * 0.01

  return f

def macros ( f, solid ):

#*****************************************************************************80
#
## macros() computes density and velocity from f().
#
#  Modified:
#
#    01 August 2026
#
#  Reference:
#
#    Ferran Alia
#    This version by John Burkardt
#
  rho      = np.sum ( f, axis = 0 )
  rho_safe = np.where ( solid, 1.0, rho )

  ux  = np.einsum ( 'i,ixy->xy', EIX, f ) / rho_safe
  uy  = np.einsum ( 'i,ixy->xy', EIY, f ) / rho_safe
#
#  Zero flow within the solid obstacle.
#
  rho[solid] = 0.0
  ux[solid]  = 0.0
  uy[solid]  = 0.0

  return rho, ux, uy

def make_solid_cylinder ( cx, cy, r ):

#*****************************************************************************80
#
## make_solid_cylinder() defines the solid obstacle.
#
#  Modified:
#
#    31 July 2026
#
#  Reference:
#
#    Ferran Alia
#    This version by John Burkardt
#
  X, Y = np.meshgrid ( np.arange(Nx), np.arange(Ny), indexing='ij' )
  solid = (X - cx)**2 + (Y - cy)**2 < r**2

  return solid

def plot_state ( rho, ux, uy, solid, step, save_dir = None ):

#*****************************************************************************80
#
## plot_state() writes a plotfile for the current state.
#
#  Modified:
#
#    01 August 2026
#
#  Reference:
#
#    Ferran Alia
#    This version by John Burkardt
#
  speed = np.sqrt ( ux**2 + uy**2 )
  speed = np.where ( solid, np.nan, speed )

  vorticity = np.gradient ( uy, axis = 0 ) \
            - np.gradient ( ux, axis = 1 )
  vorticity = np.where ( solid, np.nan, vorticity )

  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5), dpi=120)
  fig.patch.set_facecolor ( 'white' )
#
#  Compute the 99th percentile of speed, ignorning nan values inside solid.
#
  vmax = np.nanpercentile ( speed, 99 )

  im1 = ax1.imshow(speed.T, origin='lower', cmap='inferno', vmin=0, vmax=vmax)
  plt.colorbar(im1, ax=ax1, label='Speed (lattice units)')
  ax1.set_title(f'Velocity magnitude, step {step}')
  ax1.set_xlabel('x (lattice nodes)')
  ax1.set_ylabel('y (lattice nodes)')
#
#  Compute the 98th percentile of vorticity, ignorning nan values inside solid.
#
  vlim = np.nanpercentile ( np.abs(vorticity), 98 )

  norm = TwoSlopeNorm ( vmin=-vlim, vcenter=0, vmax=vlim )
  im2 = ax2.imshow(vorticity.T, origin='lower', cmap='RdBu_r', norm=norm)
  plt.colorbar(im2, ax=ax2, label='Vorticity (blue=CCW, red=CW)')
  ax2.set_title ( f'Vorticity, step {step}' )
  ax2.set_xlabel ('x (lattice nodes)' )
  ax2.set_ylabel ('y (lattice nodes)' )

  plt.tight_layout()

  if save_dir:
    os.makedirs(save_dir, exist_ok=True)
    plt.savefig(os.path.join(save_dir, f'step_{step:05d}.png'),
                bbox_inches='tight')
    plt.close()
  else:
    plt.show()
    plt.close()

  return

def stream ( f ):

#*****************************************************************************80
#
## stream() propagates each population to the neighboring node.
#
#  Modified:
#
#    31 July 2026
#
#  Reference:
#
#    Ferran Alia
#    This version by John Burkardt
#
#  Reference:
#
#    Ferran Alia,
#    The fluid simulator that doesn't solve the fluid equations,
#    Towards Data Science,
#    25 July 2026.
#
  f_new = np.empty_like ( f )

  for i in range ( 9 ):
    f_new[i] = np.roll ( 
      np.roll ( f[i], int ( EIX[i] ), axis = 0 ),
                      int ( EIY[i] ), axis = 1 )
  return f_new

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if __name__ == '__main__':
  timestamp ( )
  main ( )
  timestamp ( )

