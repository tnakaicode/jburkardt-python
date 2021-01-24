#! /usr/bin/env python3
#
def drug_dosage_plots ( ):

#*****************************************************************************80
#
## drug_dosage_plots models the variation in blood levels of a medicinal drug.
#
#  Discussion:
#
#    The blood level concentration of a medicinal drug, in mg / l, has been 
#    recorded over time.  
#
#    The concentration level must reach 800 mg / liter to be medicinally
#    effective but becomes toxic at 1000 mg / liter.
#
#    It is desired to plot the concentration level, as well as two horizontal
#    lines representing the medicinal and toxic levels.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' );
  print ( 'drug_dosage_plots:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Simulate the variation over time of the concentration' )
  print ( '  of a medicinal drug in the bloodstream.' )
#
#  Read the times and plasma levels from the data file.
#
  filename = 'drug_dosage_data.txt'
  data = np.loadtxt ( filename, delimiter = " " )
#
#  Split the data.
#
  time = data[:,0]
  level = data[:,1]
#
#  Count the number of items.
#
  N = len ( time )
#   
#  Plot the results
#
  plt.plot ( time, level, color = 'b', label =  "Plasma Concentration" )
#
#  Plot a horizontal line for the medicinal level.
#
  m_level = [ 800 ] * ( N )
  plt.plot ( time, m_level, color= 'g', label = "Medicinal Level" )
#
#  Plot a horizontal line for the toxic level.
#
  t_level = [ 1000 ] * ( N )
  plt.plot ( time, t_level, color = 'r', label = "Toxic Level" )

  plt.legend ( loc = 4 )
  plt.minorticks_on ( )
  plt.ylim ( 0, 1100 )
  plt.xlabel ( '<-- Hours -->', fontsize = 16 )
  plt.ylabel ( '<-- Concentration (mg/l) -->', fontsize = 16 )
  plt.title ( 'Drug level concentration over time.', fontsize = 16 )
#
#  Save a copy of the plot.
#
  filename = 'drug_dosage.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Display the plot.
#
  plt.show ( block = False )

  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'drug_dosage_plots:' )
  print ( '  Normal end of execution.' )

  return

if ( __name__ == '__main__' ):
  drug_dosage_plots ( )
