#! /usr/bin/env python3
#
def dosage_ode ( ):

#*****************************************************************************80
#
## dosage_ode() models the variation in blood levels of a medicinal drug.
#
#  Discussion:
#
#    Drug levels in the blood, for certain drugs, can be modeled by a set of
#    coupled first-order linear differential equations.
#
#    If we define:
#
#      A = medicine_in_intestines,
#      B = plasma_level.  
#
#    then the governing differential equations are:
#
#      dA/dt = - absorption_rate * A + intake
#      dB/dt = - excretion_rate * B + absorption_rate * A
#
#  Modified:
#
#    02 March 2021
#
#  Local:
#
#    time_step, simulation time step in hours
#    t0, starting time, in hours
#    tstop, end time, in hours
#    doses_per_day, number of doses per day
#    dosage_per_day, total daily dosage, in mg
#    absorption_rate, absorption rate constant
#    half_life, drug half life, in hours
#    blood_volume, blood volume, in liters
#    medicinal_level, level at which drug becomes effective mg/l
#    toxic_level, level at which drug becomes toxic  mg/l
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' );
  print ( 'dosage_ode():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Simulate the variation over time of the concentration' )
  print ( '  of a medicinal drug in the bloodstream.' )
#
#  Model parameters
#
  time_step = 0.25 
  t0 = 0.0
  tstop = 48.0
  doses_per_day = 1
  dosage_per_day = 7500 
  absorption_rate = 0.25 
  half_life = 6 
  blood_volume = 4.6 
  medicinal_level = 800 
  toxic_level = 1000 
#
#  Derived constants
#
  N = int ( (tstop - t0 ) / time_step )   # number of simulation steps
  dosage = dosage_per_day / doses_per_day            # amount of each dose
  dosage_interval = 24 / doses_per_day               # in hours
  excretion_rate = np.log(2) / half_life
  steps_between_doses = dosage_interval / time_step
#
#  Time-varying quantities, arrays with one value per time step
#  The syntax, "[0]*(N+1)," creates a one-dimensional array 
#  of length N+1 whose values are all zero.
#
  t = np.zeros ( N + 1 )                        # time in hours
  intake = np.zeros ( N + 1 )                   # dose at this time step
  medicine_in_intestines = np.zeros ( N + 1 )   # level of drug in intestines
  plasma_level = np.zeros ( N + 1 )             # level of drug in the blood
  plasma_concentration = np.zeros ( N + 1 )     # concentration of drug in blood
  absorption = np.zeros ( N + 1 )               # amount absorbed at this time step
  excretion = np.zeros ( N + 1 )                # amount excreted at this time step
#
#  Initialize variables - assume all others start at 0
#
  t[0] = t0
#
#  Give the first dose at the start time.
#
  step_next_dose = 1
#
#  Loop to calculate intake of drug over time, using Euler's method.
#
#  This part calculates when each dose of the drug is added, based on
#  the number of doses over a 24 hour period. The number of doses must be an
#  integer divisor of 24 for this to work.
#
  for j in range ( N ):

    t[j+1] = t[j] + time_step

    if ( j == step_next_dose ):
      intake[j] = dosage
      step_next_dose = j + steps_between_doses
    else:
      intake[j] = 0

    absorption[j] = time_step * absorption_rate * medicine_in_intestines[j]
    excretion[j] = time_step * excretion_rate * plasma_level[j]

    plasma_level[j+1] = plasma_level[j] - excretion[j] + absorption[j]
    plasma_concentration[j+1] = plasma_level[j+1] / blood_volume
    medicine_in_intestines[j+1] = medicine_in_intestines[j] - absorption[j] + intake[j]
#
#  Write plasma level to a file.
#
  filename = 'dosage_ode_levels.txt'
  output = open ( filename, 'w' )
  for j in range ( N + 1 ):
    s = str ( t[j] )
    output.write ( s )
    output.write ( ' ' )
    s = str ( plasma_concentration[j] )
    output.write ( s )
    output.write ( '\n' )
  output.close ( )
#   
#  Plot the results
#
  plt.plot ( t, plasma_concentration, color = 'b', label =  "Plasma Concentration" )

  m_level = [ medicinal_level ] * ( N + 1 )
  plt.plot ( t, m_level, color= 'g', label = "Medicinal Level" )

  t_level = [ toxic_level ] * ( N + 1 )
  plt.plot ( t, t_level, color = 'r', label = "Toxic Level" )

  plt.legend ( loc = 4 )

  plt.minorticks_on ( )
  plt.ylim ( 0, 1100 )
  plt.ylabel ( '<-- Concentration (mg/l) -->' )
  plt.xlabel ( '<-- Hours -->' )
  plt.title ( 'dosage_ode(): Drug concentration over time.\n' )
  filename = 'dosage_ode.png'
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'dosage_ode():' )
  print ( '  Normal end of execution.' )

  return

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

if ( __name__ == '__main__' ):
  timestamp ( )
  dosage_ode ( )
  timestamp ( )

