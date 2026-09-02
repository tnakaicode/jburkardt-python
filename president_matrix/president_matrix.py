#! /usr/bin/env python3
#
def president_matrix_test ( ):

#*****************************************************************************80
#
## president_matrix_test() tests president_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 May 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'president_matrix_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test president_matrix().' )

  lastname = np.array ( [ \
    "Washington", "Adams" ,    "Jefferson", "Madison",    "Monroe", \
    "Adams",      "Jackson",   "vanBuren",  "Harrison",   "Tyler", \
    "Polk",       "Taylor",    "Fillmore",  "Pierce",     "Buchanan", \
    "Lincoln",    "Johnson",   "Grant",     "Hayes",      "Garfield", \
    "Arthur",     "Cleveland", "Harrison",  "Cleveland",  "McKinley", \
    "Roosevelt",  "Taft",      "Wilson",    "Harding",    "Coolidge", \
    "Hoover",     "Roosevelt", "Truman",    "Eisenhower", "Kennedy",  \
    "Johnson",    "Nixon",     "Ford",      "Carter",     "Reagan",  \
    "Bush",       "Clinton",   "Bush",      "Obama",      "Trump", \
    "Biden",      "Trump" ] )
#
#  Evaluate the presidential lifespan adjacency matrix.
#
  A = president_matrix ( )

  pres_num = A.shape[0]
  index = np.linspace ( 1, pres_num, pres_num ) - 1
#
#  Use spy to draw an image of the matrix.
#
  plt.spy ( A, marker = "o", markersize = 4 )
  plt.grid ( True )
  plt.yticks ( index, lastname, fontsize = 6 )
  plt.title ( 'Presidential Lifespan Overlaps' )
  filename = 'president_matrix.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'president_matrix_test():' )
  print ( '  Normal end of execution.' )

  return

def president_matrix ( ):

#*****************************************************************************80
#
## president_matrix() returns a sort of presidential "adjacency" matrix.
#
#  Discussion:
#
#    Presidents I and J are "adjacent" if there was any year in which 
#    they were both alive, that is, if their lifespans overlap.
#
#    To keep things simple, we concentrate solely on birth and death years,
#    without worrying more precisely about month and day.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer A(pres_num,pres_num): A(i,j) is 1 if presidents #i and #j 
#    have overlapping lifespans.  Otherwise, the entry is 0.
#    This defines a sort of graph adjacency matrix.
#
  import numpy as np
#
#  Year of birth for each president.
#
  b = np.array ( [ \
    1732, 1735, 1743, 1751, 1758, 1767, 1767, 1782, \
    1773, 1790, 1795, 1784, 1800, 1804, 1791, 1809, \
    1808, 1822, 1822, 1831, 1829, 1837, 1833, 1837, \
    1843, 1858, 1857, 1856, 1865, 1872, 1874, 1882, \
    1884, 1890, 1917, 1908, 1913, 1913, 1924, 1911, \
    1924, 1946, 1946, 1961, 1946, 1942, 1946 ] )
#
#  Year of death for each president.
#  Currently nondead presidents are given a nominal death date.
#
  d = np.array ( [ \
    1799, 1826, 1826, 1836, 1831, 1848, 1845, 1862, \
    1841, 1862, 1849, 1850, 1874, 1869, 1868, 1865, \
    1875, 1885, 1893, 1881, 1886, 1908, 1901, 1908, \
    1901, 1919, 1930, 1924, 1923, 1933, 1964, 1945, \
    1972, 1969, 1963, 1973, 1994, 2006, 2024, 2004, \
    2018, 2050, 2050, 2050, 2050, 2050, 2050 ] )

  pres_num = len ( b )
#
#  Define the adjacency matrix.
#  We use strict inequalities here to guarantee overlap.
#
  A = np.zeros ( [ pres_num, pres_num ] )

  for pres_i in range ( 0, pres_num ):
    for pres_j in range ( 0, pres_num ):
      if ( b[pres_i] < d[pres_j] and b[pres_j] < d[pres_i] ):
        A[pres_i,pres_j] = 1

  return A

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
  president_matrix_test ( )
  timestamp ( )

