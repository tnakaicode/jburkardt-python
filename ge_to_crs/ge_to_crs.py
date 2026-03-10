#! /usr/bin/env python3
#
def crs_write ( prefix, row, col, val ):

#*****************************************************************************80
#
## crs_write() writes a CRS matrix to 3 files.
#
#  Discussion:
#
#    Three files will be created:
#    * prefix_row.txt contains N+1 row start values
#    * prefix_col.txt contains NZ column indices
#    * prefix_val.txt contains NZ matrix entries
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string PREFIX, a common prefix for the filenames.
#
#    integer ROW(N+1): the nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ): the column indices of the nonzero elements of A.
#
#    real VAL(NZ): the nonzero elements of A.
#
  import numpy as np

  filename = prefix + '_row.txt'
  np.savetxt ( filename, row )
  print ( '  Saved data as "' + filename + '"' )

  filename = prefix + '_col.txt'
  np.savetxt ( filename, col )
  print ( '  Saved data as "' + filename + '"' )

  filename = prefix + '_val.txt'
  np.savetxt ( filename, val )
  print ( '  Saved data as "' + filename + '"' )

  return

def ge_to_crs ( A ):

#*****************************************************************************80
#
## ge_to_crs() copies a GE matrix to CRS format.
#
#  Discussion:
#
#    The CRS storage format stores the nonzero entries of row I in 
#    entries ROW(I) through ROW(I+1)-1 of VAL.  
#    COL(J) records the column index of the entry in VAL(J).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,N): the matrix.
#
#  Output:
#
#    integer ROW(M+1): the nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ): the column indices of the nonzero elements of A.
#
#    real VAL(NZ): the nonzero elements of A.
#
  import numpy as np

  m, n = A.shape
  nz = np.count_nonzero ( A )
  row = np.zeros ( m + 1, dtype = int )
  col = np.zeros ( nz, dtype = int )
  val = np.zeros ( nz, dtype = float )

  row[0] = 0
  k = 0

  for i in range ( 0, m ):
    for j in range ( 0, n):
      if ( A[i,j] != 0.0 ):
        col[k] = j
        val[k] = A[i,j]
        k = k + 1

    row[i+1] = k

  return row, col, val

def ge_to_crs_risk ( ):

#*****************************************************************************80
#
## ge_to_crs_risk() converts the RISK matrix from GE to CRS format.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ge_to_crs_risk():' )
  print ( '  ge_to_crs() converts a GE matrix to CRS format.' )
  print ( '  Read a file defining the RISK matrix in GE format.' )
  print ( '  Write files defining the RISK matrix in CRS format.' )
  print ( '' )
#
#  Read file of GE data.
#
  prefix = 'risk'
  filename = prefix + '_ge.txt'
  print ( '  Reading GE file "' + filename + '"' )
  A = np.loadtxt ( filename ) 
#
#  Convert from GE to CRS format.
#
  row, col, val = ge_to_crs ( A )
#
#  Write the CRS data to files.
#
  crs_write ( prefix, row, col, val )

  return

def ge_to_crs_test ( ):

#*****************************************************************************80
#
## ge_to_crs_test() tests ge_to_crs().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ge_to_crs_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  ge_to_crs() converts a matrix from GE to CRS format.' )

  ge_to_crs_risk ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ge_to_crs_test():' )
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
  ge_to_crs_test ( )
  timestamp ( )


