#! /usr/bin/env python3
#
def state_id_from_index ( index ):

#*****************************************************************************80
#
## state_id_from_index() returns the ID of a given US state.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer index: the state index, between 1 and 50.
#
#  Output:
#
#    character*2 ident: the state ID.  
#
  import numpy as np

  id_array = np.array ( [
    'AL', \
    'AK', \
    'AZ', \
    'AR', \
    'CA', \
    'CO', \
    'CT', \
    'DE', \
    'FL', \
    'GA', \
    'HI', \
    'ID', \
    'IL', \
    'IN', \
    'IA', \
    'KS', \
    'KY', \
    'LA', \
    'ME', \
    'MD', \
    'MA', \
    'MI', \
    'MN', \
    'MS', \
    'MO', \
    'MT', \
    'NE', \
    'NV', \
    'NH', \
    'NJ', \
    'NM', \
    'NY', \
    'NC', \
    'ND', \
    'OH', \
    'OK', \
    'OR', \
    'PA', \
    'RI', \
    'SC', \
    'SD', \
    'TN', \
    'TX', \
    'UT', \
    'VT', \
    'VA', \
    'WA', \
    'WV', \
    'WI', \
    'WY' ] )

  if ( index < 0 or 50 <= index ):
    print ( '' )
    print ( 'state_id_from_index(): Fatal error!' )
    print ( '  Illegal index value =', index )
    raise Exception ( 'state_id_from_index(): Illegal index value.' )

  ident = id_array[index]

  return ident

def state_name_from_index ( index ):

#*****************************************************************************80
#
## state_name_from_index() returns the name of a given US state.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer index: the state index, between 1 and 50.
#
#  Output:
#
#    character name(): the state name.  
#
  import numpy as np

  id_array = np.array ( [ \
    'Alabama', \
    'Alaska', \
    'Arizona', \
    'Arkansas', \
    'California', \
    'Colorado', \
    'Connecticut', \
    'Delaware', \
    'Florida', \
    'Georgia', \
    'Hawaii', \
    'Idaho', \
    'Illinois', \
    'Indiana', \
    'Iowa', \
    'Kansas', \
    'Kentucky', \
    'Louisiana', \
    'Maine', \
    'Maryland', \
    'Massachusetts', \
    'Michigan', \
    'Minnesota', \
    'Mississippi', \
    'Missouri', \
    'Montana', \
    'Nebraska', \
    'Nevada', \
    'New Hampshire', \
    'New Jersey', \
    'New Mexico', \
    'New York', \
    'North Carolina', \
    'North Dakota', \
    'Ohio', \
    'Oklahoma', \
    'Oregon', \
    'Pennsylvania', \
    'Rhode Island', \
    'South Carolina', \
    'South Dakota', \
    'Tennessee', \
    'Texas', \
    'Utah', \
    'Vermont', \
    'Virginia', \
    'Washington', \
    'West Virginia', \
    'Wisconsin', \
    'Wyoming' ] )

  if ( index < 0 or 50 <= index ):
    print ( '' )
    print ( 'state_name_from_index(): Fatal error!' )
    print ( '  Illegal index value =', index )
    raise Exception ( 'state_name_from_index(): Illegal index value.' )

  name = id_array[index]

  return name

def usa_coo ( ):

#*****************************************************************************80
#
## usa_coo() returns the USA matrix in COO sparse matrix format.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real coo A(50,50): the matrix.
#
  from scipy.sparse import coo_matrix
  import numpy as np

  m = 50
  n = 50
  nzmax = 210

  i = np.array ( [ \
    1, 1, 1, 1, 3, 3, 3, 3, 4, 4, \
    4, 4, 4, 4, 5, 5, 5, 6, 6, 6, \
    6, 6, 6, 7, 7, 7, 8, 8, 8, 9, \
    9,10,10,10,10,10,12,12,12,12, \
   12,12,13,13,13,13,13,14,14,14, \
   14,15,15,15,15,15,15,16,16,16, \
   16,17,17,17,17,17,17,17,18,18, \
   18,19,20,20,20,20,21,21,21,21, \
   21,22,22,22,23,23,23,23,24,24, \
   24,24,25,25,25,25,25,25,25,25, \
   26,26,26,26,27,27,27,27,27,27, \
   28,28,28,28,28,29,29,29,30,30, \
   30,31,31,31,31,32,32,32,32,32, \
   33,33,33,33,34,34,34,35,35,35, \
   35,35,36,36,36,36,36,36,37,37, \
   37,37,38,38,38,38,38,38,39,39, \
   40,40,41,41,41,41,41,41,42,42, \
   42,42,42,42,42,42,43,43,43,43, \
   44,44,44,44,44,45,45,45,46,46, \
   46,46,46,47,47,48,48,48,48,48, \
   49,49,49,49,50,50,50,50,50,50 ], dtype = int )
  i = i - 1

  j = np.array ( [ \
    9,10,42,24,31,44,28, 5,18,24, \
   42,25,36,43, 3,28,37,31,36,16, \
   27,50,44,39,21,32,30,38,20,10, \
    1,40,33,42, 1, 9,47,37,28,44, \
   50,26,49,15,25,17,14,13,17,35, \
   22,23,41,27,25,13,49,36,25,27, \
    6,42,46,48,35,14,13,25,24, 4, \
   43,29, 8,38,48,46,29,45,32, 7, \
   39,49,14,35,34,41,15,49, 1,42, \
    4,18, 4,42,17,13,15,27,16,36, \
   12,50,41,34,16,25,15,41,50, 6, \
    3,44,12,37, 5,45,21,19,32,38, \
    8,43,36, 6, 3,38,30, 7,21,45, \
   46,42,10,40,26,41,23,22,14,17, \
   48,38,43, 4,25,16, 6,31, 5,28, \
   12,47,35,48,20, 8,30,32,21, 7, \
   33,10,27,15,23,34,26,50, 1,10, \
   33,46,17,25, 4,24,18, 4,36,31, \
    3, 6,50,12,28,32,21,29,20,48, \
   17,42,33,37,12,46,20,38,35,17, \
   23,15,13,22, 6,27,41,26,12,44 ], dtype = int )

  j = j - 1

  v = np.ones ( nzmax, dtype = int )

  A = coo_matrix ( ( v, ( i, j ) ), shape = ( m, n ), dtype = int )

  return A

def usa_ge ( ):

#*****************************************************************************80
#
## usa_ge() returns the USA matrix in dense or "general" (GE) format.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A(50,50): the matrix.
#
  Asparse = usa_coo ( )
  A = Asparse.toarray ( )

  return A

def usa_matrix_test ( ):

#*****************************************************************************80
#
## usa_matrix_test() tests usa_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 November 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'usa_matrix_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test usa_matrix()' )
#
#  Evaluate the COO matrix, and use spy() to draw an image of it.
#
  A = usa_coo ( )
  plt.spy ( A, markersize = 5.0 )
  plt.grid ( True )
  plt.title ( 'spy(): usa_coo() matrix' )
  filename = 'usa_coo.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Evaluate the GE matrix, and use spy() to draw an image of it.
#
  A = usa_ge ( )
  plt.spy ( A, markersize = 5.0 )
  plt.grid ( True )
  plt.title ( 'spy(): usa_ge() matrix' )
  filename = 'usa_ge.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Evaluate the ST matrix, and use spy() to draw an image of it.
#
  i, j, v = usa_st ( )
  k = i + j * 50
  A = np.zeros ( [ 50, 50 ] )
  n = len ( i )
  for k in range ( 0, n ):
    A[i[k],j[k]] = v[k] 

  plt.spy ( A, markersize = 5.0 )
  plt.grid ( True )
  plt.title ( 'spy(): usa_st() matrix' )
  filename = 'usa_st.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'usa_matrix_test():' )
  print ( '  Normal end of execution.' )

  return

def usa_st ( ):

#*****************************************************************************80
#
## usa_st() returns the USA matrix in sparse triplet (ST) format.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer i(210), j(210): the indices of nonzero entries. 
#
#    real v(210): the nonzero values.
#
  import numpy as np

  i = np.array ( [ \
    1, 1, 1, 1, 3, 3, 3, 3, 4, 4, \
    4, 4, 4, 4, 5, 5, 5, 6, 6, 6, \
    6, 6, 6, 7, 7, 7, 8, 8, 8, 9, \
    9,10,10,10,10,10,12,12,12,12, \
   12,12,13,13,13,13,13,14,14,14, \
   14,15,15,15,15,15,15,16,16,16, \
   16,17,17,17,17,17,17,17,18,18, \
   18,19,20,20,20,20,21,21,21,21, \
   21,22,22,22,23,23,23,23,24,24, \
   24,24,25,25,25,25,25,25,25,25, \
   26,26,26,26,27,27,27,27,27,27, \
   28,28,28,28,28,29,29,29,30,30, \
   30,31,31,31,31,32,32,32,32,32, \
   33,33,33,33,34,34,34,35,35,35, \
   35,35,36,36,36,36,36,36,37,37, \
   37,37,38,38,38,38,38,38,39,39, \
   40,40,41,41,41,41,41,41,42,42, \
   42,42,42,42,42,42,43,43,43,43, \
   44,44,44,44,44,45,45,45,46,46, \
   46,46,46,47,47,48,48,48,48,48, \
   49,49,49,49,50,50,50,50,50,50 ] )
  i = i - 1

  j = np.array ( [ \
    9,10,42,24,31,44,28, 5,18,24, \
   42,25,36,43, 3,28,37,31,36,16, \
   27,50,44,39,21,32,30,38,20,10, \
    1,40,33,42, 1, 9,47,37,28,44, \
   50,26,49,15,25,17,14,13,17,35, \
   22,23,41,27,25,13,49,36,25,27, \
    6,42,46,48,35,14,13,25,24, 4, \
   43,29, 8,38,48,46,29,45,32, 7, \
   39,49,14,35,34,41,15,49, 1,42, \
    4,18, 4,42,17,13,15,27,16,36, \
   12,50,41,34,16,25,15,41,50, 6, \
    3,44,12,37, 5,45,21,19,32,38, \
    8,43,36, 6, 3,38,30, 7,21,45, \
   46,42,10,40,26,41,23,22,14,17, \
   48,38,43, 4,25,16, 6,31, 5,28, \
   12,47,35,48,20, 8,30,32,21, 7, \
   33,10,27,15,23,34,26,50, 1,10, \
   33,46,17,25, 4,24,18, 4,36,31, \
    3, 6,50,12,28,32,21,29,20,48, \
   17,42,33,37,12,46,20,38,35,17, \
   23,15,13,22, 6,27,41,26,12,44 ] )
  j = j - 1

  v = np.ones ( 210 )

  return i, j, v

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
  usa_matrix_test ( )
  timestamp ( )

