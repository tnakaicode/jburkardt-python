#! /usr/bin/env python3
#
import numpy as np

atomic_weight_table = np.array ( [ \
    1.00797, \
    4.00260, \
    6.941, \
    9.01218, \
    10.81, \
    12.011, \
    14.0067, \
    15.9994, \
    18.998403, \
    20.179, \
    22.98977, \
    24.305, \
    26.98154, \
    28.0855, \
    30.97376, \
    32.06, \
    35.453, \
    39.948, \
    39.0983, \
    40.08, \
    44.9559, \
    47.90, \
    50.9415, \
    51.996, \
    54.9380, \
    55.847, \
    58.9332, \
    58.70, \
    63.546, \
    65.38, \
    69.72, \
    72.59, \
    74.9216, \
    78.96, \
    79.904, \
    83.80, \
    85.4678, \
    87.62, \
    88.9059, \
    91.22, \
    92.9064, \
    95.94, \
    98.00, \
    101.07, \
    102.9055, \
    106.4, \
    107.868, \
    112.41, \
    114.82, \
    118.69, \
    121.75, \
    127.60, \
    126.9045, \
    131.30, \
    132.9054, \
    137.33, \
    138.9055, \
    140.12, \
    140.9077, \
    144.24, \
    145.00, \
    150.4, \
    151.96, \
    157.25, \
    158.9254, \
    162.50, \
    164.9304, \
    167.26, \
    168.9342, \
    173.04, \
    174.967, \
    178.49, \
    180.9479, \
    183.85, \
    186.207, \
    190.2, \
    192.22, \
    195.09, \
    196.9665, \
    200.59, \
    204.37, \
    207.2, \
    208.9804, \
    209.00, \
    210.00, \
    222.00, \
    223.00, \
    226.0254, \
    227.0278, \
    232.0381, \
    231.0359, \
    238.029, \
    237.0482, \
    242.00, \
    243.00, \
    247.00, \
    247.00, \
    251.00, \
    252.00, \
    257.00, \
    258.00, \
    250.00, \
    260.00, \
    261.00, \
    262.00, \
    263.00, \
    262.00, \
    255.00, \
    256.00, \
    269.00, \
    272.00, \
    277.00, \
      0.00, \
      0.00 ] )

element_name_table = np.array ( [ \
    'Hydrogen', \
    'Helium', \
    'Lithium', \
    'Beryllium', \
    'Boron', \
    'Carbon', \
    'Nitrogen', \
    'Oxygen', \
    'Fluorine', \
    'Neon', \
    'Sodium', \
    'Magnesium', \
    'Aluminum', \
    'Silicon', \
    'Phosphorus', \
    'Sulfur', \
    'Chlorine', \
    'Argon', \
    'Potassium', \
    'Calcium', \
    'Scandium', \
    'Titanium', \
    'Vanadium', \
    'Chromium', \
    'Manganese', \
    'Iron', \
    'Cobalt', \
    'Nickel', \
    'Copper', \
    'Zinc', \
    'Gallium', \
    'Germanium', \
    'Arsenic', \
    'Selenium', \
    'Bromine', \
    'Krypton', \
    'Rubidium', \
    'Strontium', \
    'Yttrium', \
    'Zirconium', \
    'Niobium', \
    'Molybdenum', \
    'Technetium', \
    'Ruthenium', \
    'Rhodium', \
    'Palladium', \
    'Silver', \
    'Cadmium', \
    'Indium', \
    'Tin', \
    'Antimony', \
    'Tellurium', \
    'Iodine', \
    'Xenon', \
    'Cesium', \
    'Barium', \
    'Lanthanum', \
    'Cerium', \
    'Praseodymium', \
    'Neodymium', \
    'Promethium', \
    'Samarium', \
    'Europium', \
    'Gadolinium', \
    'Terbium', \
    'Dysprosium', \
    'Holmium', \
    'Erbium', \
    'Thulium', \
    'Ytterbium', \
    'Lutetium', \
    'Hafnium', \
    'Tantalum', \
    'Tungsten', \
    'Rhenium', \
    'Osmium', \
    'Iridium', \
    'Platinum', \
    'Gold', \
    'Mercury', \
    'Thallium', \
    'Lead', \
    'Bismuth', \
    'Polonium', \
    'Astatine', \
    'Radon', \
    'Francium', \
    'Radium', \
    'Actinium', \
    'Thorium', \
    'Protactinium', \
    'Uranium', \
    'Neptunium', \
    'Plutonium', \
    'Americium', \
    'Curium', \
    'Berkelium', \
    'Californium', \
    'Einsteinium', \
    'Fermium', \
    'Mendelevium', \
    'Nobelium', \
    'Lawrencium', \
    'Rutherfordium', \
    'Dubnium', \
    'Seaborgium', \
    'Bohrium', \
    'Hassium', \
    'Meitnerium', \
    'Darmstadtium', \
    'Roentgenium', \
    'Ununbiium', \
    'Ununtrium', \
    'Ununquadium' ] )

element_symbol_table = np.array ( [ \
    'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', \
    'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', \
    'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', \
    'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', \
    'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', \
    'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', \
    'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', \
    'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', \
    'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', \
    'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', \
    'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', \
    'Rg', 'Uub', 'Uut', 'Uuq' ] ) 

def elements_test ( ):

#*****************************************************************************80
#
## elements_test() tests elements().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'elements_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  elements() stores information about chemical elements.\n' );
#
#  Get data by atomic number.
#
  print ( '' )
  atno = 95
  print ( 'Atomic number =', atno )
  symbol = element_symbol ( atno = atno )
  print ( "Symbol = '" + symbol + "'" )
  name = element_name ( atno = atno )
  print ( 'Name = "' + name + '"' )
  weight = atomic_weight ( atno = atno )
  print ( 'Weight = ', weight )
#
#  Get data by symbol.
#
  print ( '' )
  symbol = 'Na'
  print ( "Symbol = '" + symbol + "'" )
  atno = atomic_number ( symbol = symbol )
  print ( 'Atomic number =', atno )
  name = element_name ( symbol = symbol )
  print ( 'Name = "' + name + '"' )
  weight = atomic_weight ( symbol = symbol )
  print ( 'Weight = ', weight )
#
#  Get data by name.
#
  print ( '' )
  name = 'Uranium'
  print ( 'Name = "' + name + '"' )
  symbol = element_symbol ( name = name )
  print ( "Symbol = '" + symbol + "'" )
  atno = atomic_number ( name = name )
  print ( 'Atomic number =', atno )
  weight = atomic_weight ( name = name )
  print ( 'Weight = ', weight )
#
#  Terminate.
#
  print ( '' )
  print ( 'elements_test():' )
  print ( '  Normal end of execution.' )

  return

def atomic_number ( name = 'None', symbol = 'None' ):

#*****************************************************************************80
#
## atomic_number() returns the atomic number.
#
#  Discussion:
#
#    Only one argument should be supplied, either atno or name.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string name: the element name.
#
#    string symbol: the element symbol.
#
#  Output:
#
#    integer atno: the atomic number.
#
  if ( name == 'None' and symbol == 'None' ):
    raise Exception ( 'atomic_number(): Fatal error, no input.' )

  if ( name != 'None' ):

    atno = -1
    for i in range ( 0, 114 ):
      if ( name == element_name_table[i] ):
        atno = i + 1
        break

  elif ( symbol != 'None' ):

    atno = -1
    for i in range ( 0, 114 ):
      if ( symbol == element_symbol_table[i] ):
        atno = i + 1
        break

  if ( atno == -1 ):
    raise Exception ( 'atomic_number(): Could not identify the element.' )

  return atno

def atomic_weight ( atno = 'None', name = 'None', symbol = 'None' ):

#*****************************************************************************80
#
## atomic_weight() returns the atomic weight.
#
#  Discussion:
#
#    Only one argument should be supplied.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer atno: the atomic number.  1 <= atno <= 114.
#
#    string name: the element name.
#
#    string symbol: the element symbol.
#
#  Output:
#
#    real weight: the atomic weight.
#
  import numpy as np

  if ( atno == 'None' and name == 'None' and symbol == 'None' ):
    raise Exception ( 'atomic_weight(): Fatal error, no input.' )

  if ( name != 'None' ):
    atno = atomic_number ( name = name )
  elif ( symbol != 'None' ):
    atno = atomic_number ( symbol = symbol )

  weight = atomic_weight_table[atno-1]

  return weight

def element_name ( atno = 'None', symbol = 'None' ):

#*****************************************************************************80
#
## element_name() returns the name of an element.
#
#  Discussion:
#
#    Only one argument should be supplied, either atno or symbol.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer atno: the atomic number.  1 <= atno <= 114.
#
#    string symbol: the element symbol.
#
#  Output:
#
#    string name: the name of the element.
#  
  if ( atno == 'None' and symbol == 'None' ):
    raise Exception ( 'element_name(): Fatal error, no input.' )

  if ( symbol != 'None' ):
    atno = atomic_number ( symbol = symbol )

  if ( atno < 1 or 114 < atno ):
    print ( 'element_name(): atno = ', atno, 'out of range.' )
    raise Exception ( 'element_name(): atno out of range.' )

  name = element_name_table[atno-1]

  return name

def element_symbol ( atno = 'None', name = 'None' ):

#*****************************************************************************80
#
## element_symbol() returns the symbol of an element.
#
#  Discussion:
#
#    Only one argument should be supplied, either atno or name.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer atno: the atomic number.  1 <= atno <= 114.
#
#    string name: the element name.
#
#  Output:
#
#    string symbol: the symbol of the element.
#  
  if ( atno == 'None' and name == 'None' ):
    raise Exception ( 'element_symbol(): Fatal error, no input.' )

  if ( name != 'None' ):
    atno = atomic_number ( name = name )

  if ( atno < 1 or 114 < atno ):
    raise Exception ( 'element_symbol(): atno out of range.' )

  symbol = element_symbol_table[atno-1]

  return symbol

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

if ( __name__ == "__main__" ):
  timestamp ( )
  elements_test ( )
  timestamp ( )

