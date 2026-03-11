#! /usr/bin/env python3
#
def absorb ( rng ):

#*****************************************************************************80
#
## absorb() determines if a colliding particle is absorbed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    Original FORTRAN77 version by Kahaner, Moler, Nash.
#    This version by John Burkardt.
#
#  Reference:
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1989,
#    ISBN: 0-13-627258-4,
#    LC: TA345.K34.
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    logical VALUE, is TRUE if the particle is absorbed.
#
#  Local:
#
#    real PA, the probability of absorption.
#
  pa = 0.1

  u = rng.random ( )

  value = ( u <= pa )

  return value

def cross_section ( e ):

#*****************************************************************************80
#
## cross_section() returns the "cross section" of a particle based on its energy.
#
#  Discussion:
#
#    The particle's cross section is a measure of its likelihood to collide
#    with the material of the slab.  This quantity typically depends on both
#    the particle's energy and the kind of medium through which it is traveling.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    Original FORTRAN77 version by Kahaner, Moler, Nash.
#    This version by John Burkardt.
#
#  Reference:
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1989,
#    ISBN: 0-13-627258-4,
#    LC: TA345.K34.
#
#  Input:
#
#    real E, the energy of the particle.
#
#  Output:
#
#    real VALUE, the cross section.
#
  import numpy as np

  s = np.abs ( np.sin ( 100.0 * ( np.exp ( e ) - 1.0 ) ) \
    + np.sin ( 18.81 * ( np.exp ( e ) - 1.0 ) ) )

  y = max ( 0.02, s )

  value = 10.0 * np.exp ( -0.1 / y )

  return value

def dist2c ( e, rng ):

#*****************************************************************************80
#
## dist2c() returns the distance to collision.
#
#  Discussion:
#
#    Assuming the particle has a given energy, and assuming it is currently
#    somewhere inside the shield, it is possible to determine a typical distance
#    which the particle can travel before it collides with the material of
#    the shield.
#
#    The computation of the collision distance is made by estimating a
#    "cross section" (as though having more energy made the particle "bigger"
#    and hence more likely to collide) and then randomly selecting a distance
#    that is logarithmically distributed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    Original FORTRAN77 version by Kahaner, Moler, Nash.
#    Tbis version by John Burkardt.
#
#  Reference:
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1989,
#    ISBN: 0-13-627258-4,
#    LC: TA345.K34.
#
#  Input:
#
#    real E, the energy of the particle.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real VALUE, the distance the particle can travel
#    through the slab before colliding.
#
  import numpy as np

  u = rng.random ( )

  value = - np.log ( u ) / cross_section ( e )

  return value

def energy ( rng ):

#*****************************************************************************80
#
## energy() assigns an energy to an emitted particle.
#
#  Discussion:
#
#    The energy E is in the range [EMIN,EMAX], with distribution
#    const/sqrt(energy).
#
#    An inverse function approach is used to compute this.
#
#    The energies are measured in MeV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    Original FORTRAN77 version by Kahaner, Moler, Nash.
#    This version by John Burkardt.
#
#  Reference:
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1989,
#    ISBN: 0-13-627258-4,
#    LC: TA345.K34.
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real VALUE, a randomly chosen energy that is
#    distributed as described above.
#
#  Local:
#
#    real EMIN, EMAX, the minimum and maximum energies.
#
  import numpy as np

  emax = 2.5
  emin = 1.0E-03

  u = rng.random ( )

  c = 1.0 / ( 2.0 * ( np.sqrt ( emax ) - np.sqrt ( emin ) ) )

  value = ( u / ( 2.0 * c ) + np.sqrt ( emin ) )
  value = value * value

  return value

def neutron_source ( rng ):

#*****************************************************************************80
#
## neutron_source() generates a new particle from the neutron source.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    Original FORTRAN77 version by Kahaner, Moler, Nash.
#    This version by John Burkardt.
#
#  Reference:
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1989,
#    ISBN: 0-13-627258-4,
#    LC: TA345.K34.
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real E, the initial energy of the particle.
#
#    real MU, the cosine of the angle between the
#    particle's direction and the X axis.
#
#    real AZM, the azimuthal angle of the particle's
#    direction.
#
#    real X, Y, Z, the initial coordinates of the particle.
#
  import numpy as np

  mu = rng.random ( )
  azm = 2.0 * np.pi * rng.random ( )

  x = 0.0
  y = 0.0
  z = 0.0

  e = energy ( rng )

  return e, mu, azm, x, y, z

def output ( na, ea, sa, nr, er, sr, nt, et, st, ntot ):

#*****************************************************************************80
#
## output() prints the results of the reactor shielding simulation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    Original FORTRAN77 version by Kahaner, Moler, Nash.
#    This version by John Burkardt.
#
#  Reference:
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1989,
#    ISBN: 0-13-627258-4,
#    LC: TA345.K34.
#
#  Input:
#
#    integer NA, number of particles absorbed by the slab.
#
#    real EA, energy absorbed by the slab.
#
#    real SA, the sum of the squares of the 
#    absorbed energies.
#
#    integer NR, number of particles reflected by the slab.
#
#    real ER, energy reflected by the slab.
#
#    real SR, the sum of the squares of the 
#    reflected energies.
#
#    integer NT, number of particles transmitted by the slab.
#
#    real ET, energy transmitted through the slab.
#
#    real ST, the sum of the squares of the 
#    transmitted energies.
#
#    integer NTOT, the total number of particles.
#
  import numpy as np

  print ( '' )
  print ( '  The Reactor Shielding Problem:' )
  print ( '' )
  print ( '                           Total                   Average' )
  print ( '                    %      Energy      Percent     Energy         StDev' )
  print ( '' )

  etot = ea + er + et

  if ( 0 < na ):
    ea_ave = ea / na
    sa = np.sqrt ( sa / na - ea_ave * ea_ave )
  else:
    ea_ave = 0.0

  pa = na * 100 / ntot

  print ( 'Absorbed     %8d  %14g  %6.2f  %14g  %14g' % ( na, ea, pa, ea_ave, sa ) )

  if ( 0 < nr ):
    er_ave = er / nr
    sr = np.sqrt ( sr / nr - er_ave * er_ave )
  else:
    er_ave = 0.0

  pr = nr * 100 / ntot

  print ( 'Reflected    %8d  %14g  %6.2f  %14g  %14g' % ( nr, er, pr, er_ave, sr ) )

  if ( 0 < nt ):
    et_ave = et / nt
    st = np.sqrt ( st / nt - et_ave * et_ave )
  else:
    et_ave = 0.0

  pt = nt * 100 / ntot

  print ( 'Transmitted  %8d  %14g  %6.2f  %14g  %14g' % ( nt, et, pt, et_ave, st ) )

  ptot = 100.0

  print ( '' )
  print ( 'Total        %8d  %14g  %6.2f' % ( ntot, etot, ptot ) )

  return

def reactor_simulation_test ( ):

#*****************************************************************************80
#
## reactor_simulation_test() tests reactor_simulation().
#
#  Discussion:
#
#    This is a Monte Carlo simulation, using uniform random numbers, which 
#    investigates the effectiveness of a shield intended to absorb the
#    neutrons emitted from a nuclear reactor.
#   
#    The reactor is modeled as a point source, located at (0,0,0).
#   
#    A particle emitted from the reactor has a random
#    initial direction, and an energy selected from
#    [Emin,Emax] with a 1/Sqrt(E) distribution.
#   
#    The shield is modeled as a wall of thickness THICK,
#    extending from 0 to THICK in the X direction, and
#    extending forever in the Y and Z directions.
#   
#    Based on the particle energy, a distance D is computed
#    which measures how far the particle could travel through
#    the shield before colliding.
#   
#    Based on the particle direction, the position is updated
#    by D units.
#   
#    If the particle is now to the left of the shield, it is
#    counted as being REFLECTED.
#   
#    If the particle is to the right of the shield, it is 
#    counted as being ABSORBED.
#   
#    If the particle is inside the shield, it has COLLIDED.
#    A particle that collides is either absorbed (end of story)
#    or SCATTERED with a new random direction and a new (lower)
#    energy.
#   
#    Every particle is followed from origin to its final fate,
#    which is reflection, transmission, or absorption.
#    At the end, a summary is printed, giving the number of
#    particles with each fate, and the average energy of each
#    group of particles.
#   
#    Increasing NTOT, the number of particles used, will improve the
#    expected reliability of the results.
#   
#    Increasing THICK, the thickness of the shield, should 
#    result in more absorptions and reflections.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    Original FORTRAN77 version by Kahaner, Moler, Nash.
#    This version by John Burkardt.
#
#  Reference:
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1989,
#    ISBN: 0-13-627258-4,
#    LC: TA345.K34.
#
#  Local:
#
#    real AZM, the azimuthal angle of the particle's direction.
#
#    real D, the distance that the particle can
#    travel through the slab, given its current energy.
#
#    real E, the energy of the particle.
#
#    real EA, energy absorbed by the slab.
#
#    real ER, energy reflected by the slab.
#
#    real ET, energy transmitted through the slab.
#
#    real MU, the cosine of the angle between the
#    particle's direction and the X axis.
#
#    integer NA, number of particles absorbed by the slab.
#
#    integer NPART, the index of the current particle.
#
#    integer NR, number of particles reflected by the slab.
#
#    integer NT, number of particles transmitted by the slab.
#
#    integer NTOT, the total number of particles to be
#    emitted from the neutron source.
#
#    real SA, standard deviation of absorbed energy.
#
#    real SR, standard deviation of reflected energy.
#
#    real ST, standard deviation of transmitted energy.
#
#    real THICK, the thickness of the slab that is
#    intended to absorb most of the particles.
#
#    real X, Y, Z, the current position of the particle.
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'reactor_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test reactor_simulation()' )

  rng = default_rng ( )

  ntot = 100000
  test_num = 5
  thick = 2.0

  print ( '' )
  print ( '  The reactor shielding simulation.' )
  print ( '  Shield thickness is THICK =', thick )
  print ( '  Number of simulated particles is NTOT =', ntot )
  print ( '  Number of tests TEST_NUM =', test_num )

  for test in range ( 0, test_num ):

    print ( '' )
    print ( '  Test #', test )
#
#  Initialize.
#
    ea = 0.0
    er = 0.0
    et = 0.0
    na = 0
    nr = 0
    nt = 0
    sa = 0.0
    sr = 0.0
    st = 0.0
#
#  Main loop over NTOT particles.
#
    for npart in range ( 0, ntot ):
#
#  Generate a new particle.
#
      e, mu, azm, x, y, z = neutron_source ( rng )

      while ( True ):
#
#  Compute the distance that the particle can travel through the slab,
#  based on its current energy.
#
        d = dist2c ( e, rng )
#
#  Update the particle's position by D units.
#
        x, y, z = update ( mu, azm, d, x, y, z )
#
#  The particle was reflected by the shield, and this path is complete.
#
        if ( x < 0.0 ):

          nr = nr + 1
          er = er + e
          sr = sr + e * e
          break
#
#  The particle was transmitted through the shield, and this path is complete.
#
        elif ( thick < x ):

          nt = nt + 1
          et = et + e
          st = st + e * e
          break
#
#  The particle collided with the shield, and was absorbed.  This path is done.
#
        else:

          absorbed = absorb ( rng )

          if ( absorbed ):

            na = na + 1
            ea = ea + e
            sa = sa + e * e
            break
#
#  The particle collided with the shield and was scattered.
#  Find the scattering angle and energy, and continue along the new path.
#
          else:

            mu, azm, e = scattering ( e, rng )
#
#  Print the results of the simulation.
#
    output ( na, ea, sa, nr, er, sr, nt, et, st, ntot )
#
#  Terminate.
#
  print ( '' )
  print ( 'reactor_simulation_test():' )
  print ( '  Normal end of execution.' )

  return

def scattering ( e, rng ):

#*****************************************************************************80
#
## scattering() returns the new direction and energy of a particle that is scattered.
#
#  Discussion:
#
#    The scattering direction is chosen uniformly on the sphere.
#
#    The energy of the scattered particle is chosen uniformly in
#    [ 0.3*E, E ].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    Original FORTRAN77 version by Kahaner, Moler, Nash.
#    This version by John Burkardt.
#
#  Reference:
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1989,
#    ISBN: 0-13-627258-4,
#    LC: TA345.K34.
#
#  Input:
#
#    real E: the particle energy before collision. 
#
#  Output:
#
#    real MU, the cosine of the angle between the
#    particle's direction and the X axis.
#
#    real AZM, the azimuthal angle of the particle's
#    direction.
#
#    real E, the particle energy after collision and scattering.
#
  import numpy as np

  mu = - 1.0 + 2.0 * rng.random ( )
  azm = 2.0 * np.pi * rng.random ( )
  u = rng.random ( )

  e = ( u * 0.7 + 0.3 ) * e

  return mu, azm, e 

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

def update ( mu, azm, d, x, y, z ):

#*****************************************************************************80
#
## update() determines the position of the particle after it has traveled D units.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    Original FORTRAN77 version by Kahaner, Moler, Nash.
#    This version by John Burkardt.
#
#  Reference:
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1989,
#    ISBN: 0-13-627258-4,
#    LC: TA345.K34.
#
#  Input:
#
#    real MU, the cosine of the angle between the
#    particle's direction and the X axis.
#
#    real AZM, the azimuthal angle of the particle's
#    direction.
#
#    real D, the distance the particle traveled.
#
#    real X, Y, Z.  The previous coordinates of the particle.  
#
#  Output:
#
#    real X, Y, Z.  The updated coordinates of the particle.
#
  import numpy as np

  s = np.sqrt ( 1.0 - mu * mu )

  x = x + d * mu
  y = y + d * s * np.cos ( azm )
  z = z + d * s * np.sin ( azm )

  return x, y, z 

if ( __name__ == "__main__" ):
  timestamp ( )
  reactor_simulation_test ( )
  timestamp ( )

