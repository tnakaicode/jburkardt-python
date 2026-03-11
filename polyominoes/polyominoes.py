#! /usr/bin/env python3
#
def cell_ij_fill ( m, i, j, color ):

#*****************************************************************************80
#
## cell_ij_fill() plots a filled (I,J) cell.
#
#  Discussion:
#
#    We assume the data is represented in a matrix.
#
#    In order to convert between the matrix coordinates and picture
#    coordinates, the (I,J) cell will be drawn with the following corners:
#
#    (j-1,m-i+1), (j,m-i+1), (j,m-i), (j-1,m-1).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the maximum row index.
#
#    integer I, J, the index of the cell.
#
#    color COLOR, can be any of the 8 abbreviated color terms
#    'r', 'g', 'b', 'c', 'm', 'y', 'w', 'k', or an RGB triple such as 
#    [1.0,0.4,0.0].  The square is filled with this color.
#
  import matplotlib.pyplot as plt

  a = j - 1
  b = j
  c = m - ( i - 1 )
  d = m - i

  plt.fill ( [ a, b, b, a ], [ c, c, d, d ], color )

  return

def cell_ij_fill_test ( ):

#*****************************************************************************80
#
## cell_ij_fill_test() tests cell_ij_fill().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 April 2018
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'cell_ij_fill_test():' )
  print ( '  cell_ij_fill() fills in unit cells indexed by (I,J)' )
  print ( '  using matrix coordinate system.' )

  mario = np.array ( [ \
   [ 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0 ], \
   [ 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0 ], \
   [ 0, 0, 6, 6, 6, 5, 5, 5, 1, 5, 0, 0, 0 ], \
   [ 0, 6, 5, 6, 5, 5, 5, 5, 1, 5, 5, 5, 0 ], \
   [ 0, 6, 5, 6, 6, 5, 5, 5, 5, 1, 5, 5, 5 ], \
   [ 0, 6, 6, 5, 5, 5, 5, 5, 1, 1, 1, 1, 0 ], \
   [ 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0 ], \
   [ 0, 0, 2, 2, 3, 2, 2, 2, 2, 0, 0, 0, 0 ], \
   [ 0, 2, 2, 2, 3, 2, 2, 3, 2, 2, 2, 0, 0 ], \
   [ 2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 0 ], \
   [ 5, 5, 2, 3, 4, 3, 3, 4, 3, 2, 5, 5, 0 ], \
   [ 5, 5, 5, 3, 3, 3, 3, 3, 3, 5, 5, 5, 0 ], \
   [ 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 0 ], \
   [ 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 0, 0, 0 ], \
   [ 0, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 0, 0 ], \
   [ 6, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 6, 0 ] ] )

  dims = mario.shape
  m = dims[0]
  n = dims[1]
#
#  0: white
#  1: black
#  2: red
#  3: blue
#  4: yellow
#  5: beige
#  6: brown
#
  plt.axis ( 'equal' )
  plt.axis ( 'off' )

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      k = mario[i,j]
#
#  Despite documentation assuring me it was possible, I could not seem to use
#  numeric RGB triples for colors.
# 
      if ( k == 0 ):
        color = 'white'
      elif ( k == 1 ):
        color = 'black'
      elif ( k == 2 ):
        color = 'red'
      elif ( k == 3 ):
        color = 'blue'
      elif ( k == 4 ):
        color = 'yellow'
      elif ( k == 5 ):
        color = 'bisque'
      elif ( k == 6 ):
        color = 'brown'

      cell_ij_fill ( m, i, j, color )

  filename = 'cell_ij_fill_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def i4mat_flip_cols ( m, n, a ):

#*****************************************************************************80
#
## i4mat_flip_cols() swaps the columns of an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an M by N array of I4's.
#
#    To "flip" the columns of an I4MAT is to start with something like
#
#      11 12 13 14 15
#      21 22 23 24 25
#      31 32 33 34 35
#      41 42 43 44 45
#      51 52 53 54 55
#
#    and return
#
#      15 14 13 12 11
#      25 24 23 22 21
#      35 34 33 32 31
#      45 44 43 42 41
#      55 54 53 52 51
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer A(M,N), the matrix to be flipped.
#
#  Output:
#
#    integer B(M,N), the flipped matrix.
#
  import numpy as np

  b = np.zeros ( [ m, n ], dtype = np.int32 )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      b[i,j] = a[i,n-1-j]

  return b

def i4mat_flip_rows ( m, n, a ):

#*****************************************************************************80
#
## i4mat_flip_rows() swaps the rows of an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an M by N array of I4's.
#
#    To "flip" the rows of an I4MAT is to start with something like
#
#      11 12 13 14 15
#      21 22 23 24 25
#      31 32 33 34 35
#      41 42 43 44 45
#      51 52 53 54 55
#
#    and return
#
#      51 52 53 54 55
#      41 42 43 44 45
#      31 32 33 34 35
#      21 22 23 24 25
#      11 12 13 14 15
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer A(M,N), the matrix to be flipped.
#
#  Output:
#
#    integer B(M,N), the flipped matrix.
#
  import numpy as np

  b = np.zeros ( [ m, n ], dtype = np.int32 )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      b[i,j] = a[m-1-i,j]

  return b

def i4mat_transpose ( m, n, a ):

#*****************************************************************************80
#
## i4mat_transpose() transposes an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer A(M,N), the matrix to be flipped.
#
#  Output:
#
#    integer B(N,M), the transposed matrix.
#
  import numpy as np

  b = np.zeros ( [ n, m ], dtype = np.int32 )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      b[j,i] = a[i,j]

  return b

def pentomino_display ( p, label ):

#*****************************************************************************80
#
## pentomino_display() displays a particular pentomino in a 5x5 grid.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 August 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P(P_M,P_N), a matrix of 0's and 1's.
#    1 <= P_M, P_N <= 5.  There should be exactly 5 values of one.
#
#    string LABEL, a title for the plot.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  The background grid.
#
  grid_m = 5
  grid_n = 5
  grid = np.zeros ( [ grid_m, grid_n ] )
#
#  Place the pentomino on the grid, so that it is "snug" in the upper left corner.
#
  dims = p.shape
  p_m = dims[0]
  p_n = dims[1]

  grid[0:p_m,0:p_n] = p[0:p_m,0:p_n]
#
#  Display each square of the grid.
#
  plt.axis ( 'equal' )
  plt.axis ( 'off' )

  for i in range ( 0, grid_m ):
    for j in range ( 0, grid_n ):

      k = grid[i,j]

      if ( k == 0 ):
        color = 'white'
      elif ( k == 1 ):
        color = 'black'

      cell_ij_fill ( grid_m, i, j, color )

  filename = label + '.png'
  print ( '  Graphics saved as "' + filename + '"' )
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  return

def pentomino_display_test ( ):

#*****************************************************************************80
#
## pentomino_display_test() tests pentomino_display().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pentomino_display_test():' )
  print ( '  pentomino_display() displays a picture of a pentomino.' )

  pentominos = np.array ( \
    [ 'F', 'I', 'L', 'N', 'P', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ] )

  for index in range ( 0, 12 ):
    name = pentominos[index]
    p = pentomino_matrix ( name )
    pentomino_display ( p, name )

  return

def pentominoes_test ( ):

#*****************************************************************************80
#
## pentominoes_test() tests pentominoes().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 April 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pentominoes_test():' )
  print ( '  Test pentominoes().' )

  cell_ij_fill_test ( )
  pentomino_matrix_test ( )
  pentomino_display_test ( )

  return

def pentomino_matrix ( name ):

#*****************************************************************************80
#
## pentomino_matrix() returns a 0/1 matrix defining a particular pentomino.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    character NAME, is f, i, l, n, p, t, u, v, w, x, y or z.
#
#  Output:
#
#    integer P(P_M,P_N), a matrix of 0's and 1's that indicates
#    the shape of the pentomino.
#
  import numpy as np

  if ( name.lower ( ) == 'f' ):

    p = np.array ( [ \
      [ 0, 1, 1 ], \
      [ 1, 1, 0 ], \
      [ 0, 1, 0 ] ] )

  elif ( name.lower ( ) == 'i' ):

    p = np.array ( [ \
      [ 1 ], \
      [ 1 ], \
      [ 1 ], \
      [ 1 ], \
      [ 1 ] ] )

  elif ( name.lower ( ) == 'l' ):

    p = np.array ( [ \
      [ 1, 0 ], \
      [ 1, 0 ], \
      [ 1, 0 ], \
      [ 1, 1 ] ] )

  elif ( name.lower ( ) == 'n' ):

    p = np.array ( [ \
      [ 1, 1, 0, 0 ], \
      [ 0, 1, 1, 1 ] ] )

  elif ( name.lower ( ) == 'p' ):

    p = np.array ( [ \
      [ 1, 1 ], \
      [ 1, 1 ], \
      [ 1, 0 ] ] )

  elif ( name.lower ( ) == 't' ):

    p = np.array ( [ \
      [ 1, 1, 1 ], \
      [ 0, 1, 0 ], \
      [ 0, 1, 0 ] ] )

  elif ( name.lower ( ) == 'u' ):

    p = np.array ( [ \
      [ 1, 0, 1 ], \
      [ 1, 1, 1 ] ] )

  elif ( name.lower ( ) == 'v' ):

    p = np.array ( [ \
      [ 1, 0, 0 ], \
      [ 1, 0, 0 ], \
      [ 1, 1, 1 ] ] )

  elif ( name.lower ( ) == 'w' ):

    p = np.array ( [ \
      [ 1, 0, 0 ], \
      [ 1, 1, 0 ], \
      [ 0, 1, 1 ] ] )

  elif ( name.lower ( ) == 'x' ):

    p = np.array ( [ \
      [ 0, 1, 0 ], \
      [ 1, 1, 1 ], \
      [ 0, 1, 0 ] ] )

  elif ( name.lower ( ) == 'y' ):

    p = np.array ( [ \
      [ 0, 0, 1, 0 ], \
      [ 1, 1, 1, 1 ] ] )

  elif ( name.lower ( ) == 'z' ):

    p = np.array ( [ \
      [ 1, 1, 0 ], \
      [ 0, 1, 0 ], \
      [ 0, 1, 1 ] ] )

  else:

    print ( '' )
    print ( 'pentomino_matrix(): Fatal error!' )
    print ( '  Illegal name = "%s"' % ( name ) )
    print ( '  Legal names: f, i, l, n, p, t, u, v, w, x, y, z.' )
    raise Exception ( 'pentomino_matrix(): Fatal error!' )

  return p

def pentomino_matrix_test ( ):

#*****************************************************************************80
#
## pentomino_matrix_test() tests pentomino_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pentomino_matrix_test():' )
  print ( '  pentomino_matrix() returns a 0/1 matrix representing a pentomino.' )

  pentominos = np.array ( \
    [ 'F', 'I', 'L', 'N', 'P', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ] )

  for index in range ( 0, 12 ):
    name = pentominos[index]
    p = pentomino_matrix ( name )
    dims = p.shape
    m = dims[0]
    n = dims[1]
    print ( '' )
    print ( '  %s pentomino (%d,%d):' % ( name, m, n ) )
    print ( '' )
    for i in range ( 0, m ):
      print ( '    ', end = '' )
      for j in range ( 0, n ):
        print ( ' %d' % ( p[i,j] ), end = '' )
      print ( '' )

  return

def polyomino_condense ( mp, np, p ):

#*****************************************************************************80
#
## polyomino_condense() condenses a polyomino.
#
#  Discussion:
#
#    A polyomino is a shape formed by connecting unit squares edgewise.
#
#    A polyomino can be represented by an MxN matrix, whose entries are
#    1 for squares that are part of the polyomino, and 0 otherwise.
#
#    This program is given an MxN matrix that is meant to represent a 
#    polyomino.  It first replaces all nonzero entries by the value 1.
#    It then "condenses" the matrix, if possible, by removing initial and
#    final rows and columns that are entirely zero.
#
#    While this procedure might save a slight amount of space, its purpose
#    is to simplify the task of manipulating polyominos, embedding them in
#    larger shapes, and detecting whether two polyominos describe the same
#    shape.
#
#    It is entirely possible, and usual, that the output quantities are
#    simply copies of the input quantities.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer MP, NP, the number of rows and columns in the representation
#    of the polyomino P.
#
#    integer P(MP,NP), a matrix of 0's and 1's representing the 
#    polyomino.  
#
#  Output:
#
#    integer MQ, NQ, the number of rows and columns of the
#    condensed polyomino.
#
#    integer Q(MQ,NQ), the representation of the condensed
#    polyomino.
#
  import numpy
#
#  Discard nonsense.
#
  if ( mp <= 0 or np <= 0 ):
    mq = 0
    nq = 0
    q = numpy.zeros ( [ 0, 0 ] )
    return mq, nq, q
#
#  Seek first and last nonzero rows, columns.
#
  i_min = -1
  for i in range ( 0, mp ):
    for j in range ( 0, np ):
      if ( p[i,j] != 0 ):
        i_min = i
        break
    if ( i_min != -1 ):
      break
#
#  If I_MIN = -1, then we have a null matrix.
#
  if ( i_min == -1 ):
    mq = 0
    nq = 0
    q = numpy.zeros ( [ 0, 0 ] )
    return mq, nq, q

  i_max = mp
  for i in range ( mp - 1, -1, -1 ):
    for j in range ( 0, np ):
      if ( p[i,j] != 0 ):
        i_max = i
        break
    if ( i_max != mp ):
      break

  j_min = -1
  for j in range ( 0, np ):
    for i in range ( 0, mp ):
      if ( p[i,j] != 0 ):
        j_min = j
        break
    if ( j_min != -1 ):
      break

  j_max = np
  for j in range ( np - 1, -1, -1 ):
    for i in range ( 0, mp ):
      if ( p[i,j] != 0 ):
        j_max = j
        break
    if ( j_max != np ):
      break
#
#  Measure the nonzero block.
#
  mq = i_max + 1 - i_min
  nq = j_max + 1 - j_min
  q = numpy.zeros ( [ mq, nq ] )
#
#  Copy the nonzero block.
#
  for j in range ( 0, nq ):
    for i in range ( 0, mq ):
      if ( p[i+i_min,j+j_min] != 0 ):
        q[i,j] = 1
      else:
        q[i,j] = 0

  return mq, nq, q

def polyomino_condense_test ( ):

#*****************************************************************************80
#
## polyomino_condense_test() tests polyomino_condense().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Local:
#
#    integer MP, NP, the number of rows and columns in the representation
#    of the polyomino P.
#
#    integer P(MP,NP), a matrix representing the polyomino.  
#
  import numpy
  import platform

  print ( '' )
  print ( 'polyomino_condense_test:' )
  print ( '  polyomino_condense "cleans up" a matrix that is supposed' )
  print ( '  to represent a polyomino:' )
  print ( '  * nonzero entries are set to 1:' )
  print ( '  * initial and final zero rows and columns are deleted.' )
#
#  Nothing happens:
#
  mp = 3
  np = 3
  p = numpy.array ( [ \
    [ 0, 1, 1 ], \
    [ 1, 1, 0 ], \
    [ 0, 1, 0 ] ] )
  polyomino_condense_demo ( mp, np, p )
#
#  Nonzero, but non-one entries are set to 1.
#
  mp = 3
  np = 3
  p = numpy.array ( [ \
    [ 0,  1, 2 ], \
    [ 1,  3, 0 ], \
    [ 0, -9, 0 ] ] )
  polyomino_condense_demo ( mp, np, p )
#
#  Extraneous zero rows and columns are removed.
#
  mp = 3
  np = 4
  p = numpy.array ( [ \
    [ 0, 0, 0, 0 ], \
    [ 1, 3, 0, 0 ], \
    [ 0, 0, 0, 0 ] ] )
  polyomino_condense_demo ( mp, np, p )
#
#  Null matrices are detected.
#
  mp = 2
  np = 4
  p = numpy.array ( [ \
    [ 0, 0, 0, 0 ], \
    [ 0, 0, 0, 0 ] ] )
  polyomino_condense_demo ( mp, np, p )

  return

def polyomino_condense_demo ( mp, np, p ):

#*****************************************************************************80
#
## polyomino_condense_demo() demonstrates the result of calling polyomino_condense.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer MP, NP, the number of rows and columns in the representation
#    of the polyomino P.
#
#    integer P(MP,NP), a matrix representing the polyomino.  
#
#  Local:
#
#    integer MQ, NQ, the number of rows and columns in the representation
#    of the condensed polyomino Q.
#
#    integer Q(MQ,NQ), a matrix representing the condensed polyomino.  
#
  label = '  The initial (%d,%d) polynomino P:' % ( mp, np )
  polyomino_print ( mp, np, p, label )

  mq, nq, q = polyomino_condense ( mp, np, p )

  label = '  The condensed (%d,%d) polynomino Q:' % ( mq, nq )
  polyomino_print ( mq, nq, q, label )

  return

def polyomino_embed_list ( mr, nr, r, mp, np, p, number ):

#*****************************************************************************80
#
## polyomino_embed_list() lists the polyomino embeddings in a region.
#
#  Discusion:
#
#    A region R is a subset of an MRxNR grid of squares.
#
#    A polyomino P is a subset of an MPxNP grid of squares.
#
#    Both objects are represented by binary matrices, with the property that
#    there are no initial or final zero rows or columns.
#
#    For this computation, we regard P as a "fixed" polyomino in other words,
#    no reflections or rotations will be allowed.
#
#    An "embedding" of P into R is an offset (MI,NJ) such that 
#      P(I,J) = R(I+MI,J+NJ) 
#      for 1 <= I <= MP, 1 <= J <= NP, and 
#      for 0 <= MI <= MR-MP, 0 <= MJ <= NR-NP.
#    We can detect an embedding simply by taking what amounts to a kind of
#    dot product of P with a corresponding subregion of R.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer MR, NR, the number of rows and columns in the representation
#    of the region R.
#
#    integer R(MR,NR), a matrix of 0's and 1's representing the 
#    region.
#
#    integer MP, NP, the number of rows and columns in the representation
#    of the polyomino P.
#
#    integer P(MP,NP), a matrix of 0's and 1's representing the 
#    polyomino.
#
#    integer NUMBER, the number of embeddings.
#
#  Output:
#
#    integer EMBED_list(NUMBER,2), for each embedding, the I and J 
#    offsets applied to the polyomino P.
#
  import numpy as numpy

  embed_list = numpy.zeros ( [ number, 2 ], dtype = numpy.int32 )
#
#  Count the 1's in P.
#
  pr = sum ( sum ( p ) )
#
#  For each possible (I,J) coordinate of the upper left corner of a subset of R,
#  see if it matches P.
#
  k = 0
  for mi in range ( 0, mr - mp + 1 ):
    for nj in range ( 0, nr - np + 1 ):
      srp = 0
      for i in range ( 0, mp ):
        for j in range ( 0, np ):
          srp = srp + p[i,j] * r[i+mi,j+nj]
      if ( srp == pr ):
        embed_list[k,0] = mi
        embed_list[k,1] = nj
        k = k + 1

  return embed_list

def polyomino_embed_list_test ( ):

#*****************************************************************************80
#
## polyomino_embed_list_test() tests polyomino_embed_list().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as numpy

  print ( '' )
  print ( 'polyomino_embed_list_test:' )
  print ( '  polyomino_embed_list lists the offsets used' )
  print ( '  to embed a fixed polyomino in a region.' )

  mr = 4
  nr = 4
  r = numpy.array ( [ \
    [ 0, 1, 1, 1 ], \
    [ 1, 1, 0, 1 ], \
    [ 1, 1, 1, 1 ], \
    [ 1, 0, 1, 1 ] ] )

  polyomino_print ( mr, nr, r, '  The given region R:' )

  mp = 3
  np = 2
  p = numpy.array ( [ \
    [ 0, 1 ], \
    [ 0, 1 ], \
    [ 1, 1 ] ] )

  polyomino_print ( mp, np, p, '  The given polyomino P:' )
#
#  Get the number of embeddings.
#
  number = polyomino_embed_number ( mr, nr, r, mp, np, p )

  print ( '' )
  print ( '  As a fixed polyomino, P can be embedded in R in %d ways' % ( number ) )
#
#  Get the list of embeddings.
#
  embed_list = polyomino_embed_list ( mr, nr, r, mp, np, p, number )

  for k in range ( 0, number ):
    mk = embed_list[k,0]
    nk = embed_list[k,1]
    mq = mr
    nq = nr
    q = r.copy ( )
    for i in range ( 0, mp ):
      for j in range ( 0, np ):
        q[i+mk,j+nk] = q[i+mk,j+nk] + p[i,j]
    print ( '' )
    print ( '  Embedding number %d:' % ( k ) )
    print ( '' )
    for i in range ( 0, mq ):
      for j in range ( 0, nq ):
        print ( ' %d' % ( q[i,j] ), end = '' )
      print ( '' )

  return

def polyomino_embed_number ( mr, nr, r, mp, np, p ):

#*****************************************************************************80
#
## polyomino_embed_number() counts the number of polyomino embeddings in a region.
#
#  Discusion:
#
#    A region R is a subset of an MRxNR grid of squares.
#
#    A polyomino P is a subset of an MPxNP grid of squares.
#
#    Both objects are represented by binary matrices, with the property that
#    there are no initial or final zero rows or columns.
#
#    For this computation, we regard P as a "fixed" polyomino in other words,
#    no reflections or rotations will be allowed.
#
#    An "embedding" of P into R is an offset (MI,NJ) such that 
#      P(I,J) = R(I+MI,J+NJ) 
#      for 1 <= I <= MP, 1 <= J <= NP, and 
#      for 0 <= MI <= MR-MP, 0 <= MJ <= NR-NP.
#    We can detect an embedding simply by taking what amounts to a kind of
#    dot product of P with a corresponding subregion of R.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer MR, NR, the number of rows and columns in the representation
#    of the region R.
#
#    integer R(MR,NR), a matrix of 0's and 1's representing the 
#    region.
#
#    integer MP, NP, the number of rows and columns in the representation
#    of the polyomino P.
#
#    integer P(MP,NP), a matrix of 0's and 1's representing the 
#    polyomino.
#
#  Output:
#
#    integer NUMBER, the number of distinct embeddings of P into R.
#
  number = 0
#
#  Count the 1's in P.
#
  pr = sum ( sum ( p ) )
#
#  For each possible (I,J) coordinate of the upper left corner of a subset of R,
#  see if it matches P.
#
  for mi in range ( 0, mr - mp + 1 ):
    for nj in range ( 0, nr - np + 1 ):
      srp = 0
      for i in range ( 0, mp ):
        for j in range ( 0, np ):
          srp = srp + p[i,j] * r[i+mi,j+nj]
      if ( srp == pr ):
        number = number + 1
 
  return number

def polyomino_embed_number_test ( ):

#*****************************************************************************80
#
## polyomino_embed_number_test() tests polyomino_embed_number().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy

  print ( '' )
  print ( 'polyomino_embed_number_test:' )
  print ( '  polyomino_embed_number reports the number of ways a' )
  print ( '  fixed polyomino can be embedded in a region.' )

  mr = 4
  nr = 4
  r = numpy.array ( [ \
    [ 0, 1, 1, 1 ], \
    [ 1, 1, 0, 1 ], \
    [ 1, 1, 1, 1 ], \
    [ 1, 0, 1, 1 ] ] )

  polyomino_print ( mr, nr, r, '  The given region R:' )

  mp = 3
  np = 2
  p = numpy.array ( [ \
    [ 0, 1 ], \
    [ 0, 1 ], \
    [ 1, 1 ] ] )

  polyomino_print ( mp, np, p, '  The given polyomino P:' )

  number = polyomino_embed_number ( mr, nr, r, mp, np, p )

  print ( '' )
  print ( '  As a fixed polyomino, P can be embedded in R in %d ways.' % ( number ) )

  return

def polyomino_embed_test ( ):

#*****************************************************************************80
#
## polyomino_embed_test() tests polyomino_embed().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'polyomino_embed_test:' )
  print ( '  Test polyomino_embed().' )

  polyomino_embed_number_test ( )
  polyomino_embed_list_test ( )

  return

def polyomino_enumerate_chiral ( n_data ):

#*****************************************************************************80
#
## polyomino_enumerate_chiral() counts chiral polyominoes (allowing holes).
#
#  Discussion:
#
#    Polyominoes are connected planar shapes formed by adjoining unit squares.
#
#    The number of unit squares in a polyomino is its order.
#
#    If we ignore reflections and rotations when comparing polyominoes,
#    then we are considering the class of "chiral" polyominoes.  In that case,
#    for instance, there are just 18 chiral polyominoes of order 5.
#
#    As the order increases, the number of polyominoes grows very rapidly.
#    The list offered here goes no further than order 28, but the later
#    numbers in the list are too large to represent as 32 byte integers. 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2018
#
#  Author:
#

#    John Burkardt
#
#  Reference:
#
#    Solomon Golomb,
#    Polyominoes: Puzzles, Patterns, Problems, and Packings,
#    Princeton University Press, 1996,
#    ISBN: 9780691024448
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#    Thereafter, the input value should be the output value from the
#    previous call.
#
#  Output:
#
#    integer N_DATA, the input value, incremented by 1, unless there is
#    no more data, in which case the output value will be 0 again.
#
#    integer ORDER, the order of a polyomino.
#
#    integer NUMBER, the number of chiral polyominos of this order.
#
  import numpy as np

  n_max = 31

  order_vec = np.array ( [ \
    0, \
    1,  2,  3,  4,  5, \
    6,  7,  8,  9, 10, \
   11, 12, 13, 14, 15, \
   16, 17, 18, 19, 20, \
   21, 22, 23, 24, 25, \
   26, 27, 28, 29, 30 ] )

  number_vec = np.array ( [ \
    1, \
    1, 1, 2, 7, 18, \
    60, 196, 704, 2500, 9189, \
    33896, 126759, 476270, 1802312, 6849777, \
    26152418, 100203194, 385221143, 1485200848, 5741256764, \
    22245940545, 86383382827, 336093325058, 1309998125640, 5114451441106, \
    19998172734786, 78306011677182, 307022182222506, 1205243866707468, 4736694001644862 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    order = 0
    number = 0
  else:
    order = order_vec[n_data]
    number = number_vec[n_data]
    n_data = n_data + 1

  return n_data, order, number

def polyomino_enumerate_chiral_test ( ):

#*****************************************************************************80
#
## polyomino_enumerate_chiral_test() tests polyomino_enumerate_chiral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'polyomino_enumerate_chiral_test:' )
  print ( '  polyomino_enumerate_chiral returns counts of' )
  print ( '  the number of chiral polyominoes.' )
  print ( '' )
  print ( '     Order     Number' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, order, number = polyomino_enumerate_chiral ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %d  %d' % (  order, number ) )

  return

def polyomino_enumerate_fixed ( n_data ):

#*****************************************************************************80
#
## polyomino_enumerate_fixed() counts fixed polyominoes (allowing holes).
#
#  Discussion:
#
#    Polyominoes are connected planar shapes formed by adjoining unit squares.
#
#    The number of unit squares in a polyomino is its order.
#
#    If we do not ignore reflections and rotations when comparing polyominoes,
#    then we are considering the class of "fixed" polyominoes.  In that case,
#    for instance, there are 65 fixed polyominoes of order 5.
#
#    As the order increases, the number of polyominoes grows very rapidly.
#    The list offered here goes no further than order 28, but the later
#    numbers in the list are too large to represent as 32 byte integers. 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Solomon Golomb,
#    Polyominoes: Puzzles, Patterns, Problems, and Packings,
#    Princeton University Press, 1996,
#    ISBN: 9780691024448
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#    Thereafter, the input value should be the output value from the
#    previous call.
#
#  Output:
#
#    integer N_DATA, the input value, incremented by 1, unless there is
#    no more data, in which case the output value will be 0 again.
#
#    integer ORDER, the order of a polyomino.
#
#    integer NUMBER, the number of fixed polyominos of this order.
#
  import numpy as np

  n_max = 29

  order_vec = np.array ( [ \
    0, \
    1,  2,  3,  4,  5, \
    6,  7,  8,  9, 10, \
   11, 12, 13, 14, 15, \
   16, 17, 18, 19, 20, \
   21, 22, 23, 24, 25, \
   26, 27, 28 ] )

  number_vec = np.array ( [  \
    1, \
    1, 2, 6, 19, 63,  \
    216, 760, 2725, 9910, 36446,  \
    135268, 505861, 1903890, 7204874, 27394666,  \
    104592937, 400795844, 1540820542, 5940738676, 22964779660,  \
    88983512783, 345532572678, 1344372335524, 5239988770268, 20457802016011,  \
    79992676367108, 313224032098244, 1228088671826973 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    order = 0
    number = 0
  else:
    order = order_vec[n_data]
    number = number_vec[n_data]
    n_data = n_data + 1

  return n_data, order, number

def polyomino_enumerate_fixed_test ( ):

#*****************************************************************************80
#
## polyomino_enumerate_fixed_test() tests polyomino_enumerate_fixed().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'polyomino_enumeratev_fixed_test:' )
  print ( '  polyomino_enumerate_fixed returns counts of' )
  print ( '  the number of fixed polyominoes.' )
  print ( '' )
  print ( '     Order     Number' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, order, number = polyomino_enumerate_fixed ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %d  %d' % (  order, number ) )

  return

def polyomino_enumerate_free ( n_data ):

#*****************************************************************************80
#
## polyomino_enumerate_free() counts free polyominoes (allowing holes).
#
#  Discussion:
#
#    Polyominoes are connected planar shapes formed by adjoining unit squares.
#
#    The number of unit squares in a polyomino is its order.
#
#    If we ignore reflections and rotations when comparing polyominoes,
#    then we are considering the class of "free" polyominoes.  In that case,
#    for instance, there are just 12 free polyominoes of order 5, the
#    so called "pentominoes".
#
#    As the order increases, the number of polyominoes grows very rapidly.
#    The list offered here goes no further than order 28, but the later
#    numbers in the list are too large to represent as 32 byte integers. 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Solomon Golomb,
#    Polyominoes: Puzzles, Patterns, Problems, and Packings,
#    Princeton University Press, 1996,
#    ISBN: 9780691024448
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#    Thereafter, the input value should be the output value from the
#    previous call.
#
#  Output:
#
#    integer N_DATA, the input value, incremented by 1, unless there is
#    no more data, in which case the output value will be 0 again.
#
#    integer ORDER, the order of a polyomino.
#
#    integer NUMBER, the number of free polyominos of this order.
#
  import numpy as np

  n_max = 29

  order_vec = np.array ( [ \
    0, \
    1,  2,  3,  4,  5, \
    6,  7,  8,  9, 10, \
   11, 12, 13, 14, 15, \
   16, 17, 18, 19, 20, \
   21, 22, 23, 24, 25, \
   26, 27, 28 ] )

  number_vec = np.array ( [ \
    1, \
    1,  1,  2,  5,  12, \
    35,  108,  369,  1285,  4655, \
    17073,  63600,  238591,  901971,  3426576, \
    13079255,  50107909,  192622052,  742624232,  2870671950, \
    11123060678,  43191857688,  168047007728,  654999700403,  2557227044764, \
    9999088822075,  39153010938487,  153511100594603 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    order = 0
    number = 0
  else:
    order = order_vec[n_data]
    number = number_vec[n_data]
    n_data = n_data + 1

  return n_data, order, number

def polyomino_enumerate_free_test ( ):

#*****************************************************************************80
#
## polyomino_enumerate_free_test() tests polyomino_enumerate_free().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'polyomino_enumerate_free_test:' )
  print ( '  polyomino_enumerate_free returns counts of' )
  print ( '  the number of free polyominoes.' )
  print ( '' )
  print ( '     Order     Number' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, order, number = polyomino_enumerate_free ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %d  %d' % (  order, number ) )

  return

def polyomino_enumerate_test ( ):

#*****************************************************************************80
#
## polyomino_enumerate_test() tests polyomino_enumerate().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 May 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'polyomino_enumerate_test:' )
  print ( '  polyomino_enumerate counts various kinds of polyominoes.' )

  polyomino_enumerate_chiral_test ( )
  polyomino_enumerate_fixed_test ( )
  polyomino_enumerate_free_test ( )

  return

def polyomino_index ( m, n, p ):

#*****************************************************************************80
#
## polyomino_index() assigns an index to each nonzero entry of a polyomino.
#
#  Example:
#
#    P = 
#      1 0 1 1
#      1 1 1 0
#      0 1 1 0
#
#    PIN =
#      1 0 2 3
#      4 5 6 0
#      0 7 8 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 May 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the representation
#    of the polyomino P.
#
#    integer P(M,N), the polyomino.  It is assumed that every entry
#    is a 0 or a 1.
#
#  Output:
#
#    integer PIN(M,N), the index of each nonzero entry.
#
  import numpy as np

  pin = np.zeros ( [ m, n ] )

  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( p[i,j] != 0 ):
        k = k + 1
        pin[i,j] = k

  return pin

def polyomino_index_test ( ):

#*****************************************************************************80
#
## polyomino_index_test() tests polyomino_index().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'polyomino_index_test' )
  print ( '  polyomino_index assigns an index to each nonzero entry' )
  print ( '  of a polyomino.' )

  m = 3
  n = 4

  p = np.array ( [ \
    [ 1, 0, 1, 1 ], \
    [ 1, 1, 1, 0 ], \
    [ 0, 1, 1, 0 ] ] )

  polyomino_print ( m, n, p, '  The polyomino P:' )

  pin = polyomino_index ( m, n, p )

  print ( '' )
  print ( '  PIN: Index vector for P:' )
  print ( '' )
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      print ( ' %d' % ( pin[i,j] ), end = '' )
    print ( '' )

  return

def polyomino_lp_write ( filename, label, m, n, a, b ):

#*****************************************************************************80
#
## polyomino_lp_write() writes an LP file for the polyomino problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the output filename.
#
#    string LABEL, the problem title.
#
#    integer M, the number of equations
#
#    integer N, the number of variables.
#
#    integer A(M,N), the coefficients.
#
#    integer B(M), the right hand sides.
#

#
#  Open the file.
#
  output = open ( filename, 'w' )

  output.write ( '%s\n' % ( label ) )
  output.write ( '\n' )
 
  output.write ( 'Maximize\n' )
  output.write ( '  Obj: 0\n' )

  output.write ( 'Subject to\n' )

  for i in range ( 0, m ):

    first = True

    for j in range ( 0, n ):

      if ( a[i,j] != 0 ):

        if ( a[i,j] < 0 ):
          output.write ( ' -' )
        elif ( not first ):
          output.write ( ' +' )

        if ( abs ( a[i,j] ) == 1 ):
          s = ' x%d' % j
          output.write ( s )
        else:
          s = ' %d x%d' % ( abs ( a[i,j] ), j )
          output.write ( s )

        first = False

    s = ' = %d\n' % ( b[i] )
    output.write ( s )

  output.write ( 'Binary\n' )
  output.write ( ' ' )
  for j in range ( 0, n ):
    s = ' x%d' % ( j )
    output.write ( s )
  output.write ( '\n' )

  output.write ( 'End\n' )
#
#  Close the file.
#
  output.close ( )

  return

def polyomino_lp_write_test ( ):

#*****************************************************************************80
#
## polyomino_lp_write_test() tests polyomino_lp_write().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'polyomino_lp_write_test:' )
  print ( '  polyomino_lp_write writes an LP file associated' )
  print ( '  with a binary programming problem for tiling a region' )
  print ( '  with copies of a single polyomino.' )
#
#  Get the coefficients and right hand side for the Reid system.
#
  a, b = polyomino_monohedral_example_reid_system ( )
#
#  Create the LP file.
#
  filename = 'reid.lp'
  label = '\ LP file for the Reid example.'
  shape = a.shape
  m = shape[0]
  n = shape[1]

  polyomino_lp_write ( filename, label, m, n, a, b )

  print ( '' )
  print ( '  polyomino_lp_write created the LP file "%s"' % ( filename ) )

  return

def polyomino_monohedral_example_reid_system ( ):

#*****************************************************************************80
#
## polyomino_monohedral_example_reid_system() sets up the Reid linear system.
#
#  Discussion:
#
#    This function sets up the linear system A*x=b associated with
#    the Reid polyomino tiling problem.
#
#    While it is desirable to have a general procedure that can automatically
#    deduce the linear system from the problem specification, for simplicity
#    in this example, we simply provide the linear system directly.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2018
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer A(9,10), the system matrix.
#
#    integer B(9), the right hand side.
#
  import numpy as np

  a = np.array ( [ \
    [1,0,0,0,0,1,0,0,0,0], \
    [1,0,0,0,0,0,1,0,0,0], \
    [0,1,0,0,0,1,0,1,0,0], \
    [0,1,1,0,0,0,1,0,1,0], \
    [0,0,1,0,0,0,0,0,0,1], \
    [0,0,0,1,0,0,0,1,0,0], \
    [0,0,0,1,1,0,0,0,1,0], \
    [0,0,0,0,1,0,0,0,0,1], \
    [2,2,2,2,2,2,2,2,2,2] ] )

  b = np.array ( [ 1,1,1,1,1,1,1,1,8] )

  return a, b

def polyomino_print ( m, n, p, label ):

#*****************************************************************************80
#
## polyomino_print() prints a polyomino.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the representation
#    of the polyomino P.
#
#    integer P(M,N), a matrix of 0's and 1's representing the 
#    polyomino.  The matrix should be "tight", that is, there should be a
#    1 in row 1, and in column 1, and in row M, and in column N.
#
#    string LABEL, a title for the polyomino.
#
  print ( '' )
  print ( label )
  print ( '' )
  if ( m <= 0 or n <= 0 ):
    print ( '  [ Null matrix ]' )
  else:
    for i in range ( 0, m ):
      for j in range ( 0, n ):
        print ( ' %d' % ( p[i,j] ), end = '' )
      print ( '' )

  return

def polyomino_print_test ( ):

#*****************************************************************************80
#
## polyomino_print_test() tests polyomino_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'polyomino_print_test:' )
  print ( '  polyomino_print prints a polyomino.' )

  m = 3
  n = 4

  p = np.array ( [ \
    [ 1, 0, 1, 1 ], \
    [ 1, 1, 1, 0 ], \
    [ 0, 1, 1, 0 ] ] )

  label = 'A sample polyomino'

  polyomino_print ( m, n, p, label )

  print ( '' )
  print ( 'polyomino_print_test:' )
  print ( '  Normal end of execution.' )

  return

def polyomino_transform ( m, n, p, rotate, reflect ):

#*****************************************************************************80
#
## polyomino_transform() transforms a polyomino.
#
#  Discussion:
#
#    A polyomino can be rotated or reflected.
#
#    This program is given a polyomino and returns the resulting polyomino
#    after the specified reflection and rotation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the representation
#    of the polyomino P.
#
#    integer P(M,N), a matrix of 0's and 1's representing the 
#    polyomino.  The matrix should be "tight", that is, there should be a
#    1 in row 1, and in column 1, and in row M, and in column N.
#
#    integer ROTATE, is 0, 1, 2, or 3, the number of 90 degree
#    counterclockwise rotations to be applied.
#
#    integer REFLECT, is 0 or 1.  If it is 1, then each row of the
#    polyomino matrix is to be reflected before any rotations are performed.
#
#  Output:
#
#    integer MQ, NQ, the number of rows and columns of the
#    representation of the transformed polyomino
#
#    integer Q(MQ,NQ), the representation of the transformed
#    polyomino.
#
  import numpy as np

  mq = m
  nq = n
  q = np.copy ( p )

  reflect = ( reflect % 2 )

  if ( reflect == 1 ):
    q = i4mat_flip_cols ( mq, nq, q )    

  rotate = ( rotate % 4 )

  for k in range ( 0, rotate ):
    q = i4mat_transpose ( mq, nq, q )
    r = mq
    s = nq
    mq = s
    nq = r

    q = i4mat_flip_rows ( mq, nq, q )

  return mq, nq, q

def polyomino_transform_test ( ):

#*****************************************************************************80
#
## polyomino_transform_test() tests polyomino_transform().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Local:
#
#    integer M, N, the number of rows and columns in the representation
#    of the polyomino P.
#
#    integer P(M,N), a matrix of 0's and 1's representing the 
#    polyomino.  The matrix should be "tight", that is, there should be a
#    1 in row 1, and in column 1, and in row M, and in column N.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'polyomino_transform_test:' )
  print ( '  polyomino_transform can transform a polyomino.' )
  print ( '  Generate all 8 combinations of rotation and reflection' )
  print ( '  applied to a polyomino represented by a binary matrix.' )

  m = 3
  n = 3
  p = np.array ( [ \
    [ 0, 1, 1 ], \
    [ 1, 1, 0 ], \
    [ 0, 1, 0 ] ] )

  polyomino_print ( m, n, p, '  The given polyomino P' )

  for reflect in range ( 0, 2 ):
    for rotate in range ( 0, 4 ):

      mq, nq, q = polyomino_transform ( m, n, p, rotate, reflect )
      label = '  P after %d reflections and %d rotations:' % ( reflect, rotate )
      polyomino_print ( mq, nq, q, label )

  return

def polyominoes_test ( ):

#*****************************************************************************80
#
## polyominoes_test() tests polyominoes().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'polyominoes_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test polyominoes().' )

  pentominoes_test ( )
  polyomino_condense_test ( )
  polyomino_embed_test ( )
  polyomino_enumerate_test ( )
  polyomino_index_test ( )
  polyomino_lp_write_test ( )
  polyomino_transform_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'polyominoes_test' )
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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## timestamp_test() tests timestamp().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'timestamp_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  timestamp() prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  polyominoes_test ( )
  timestamp ( )

