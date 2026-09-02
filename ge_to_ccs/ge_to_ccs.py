#! /usr/bin/env python3
#
def ge_to_ccs_test ( ):

#*****************************************************************************80
#
## ge_to_ccs_test() tests ge_to_ccs().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ge_to_ccs_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  ge_to_ccs() converts a matrix from GE to CCS format.' )

  ge_to_ccs_risk ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ge_to_ccs_test():' )
  print ( '  Normal end of execution.' )

  return

def ccs_write ( prefix, rowind, colptr, a ):

#*****************************************************************************80
#
## ccs_write() writes a CCS matrix to three files.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    string prefix: defines the names of the
#    files containing the column pointers, row entries, and matrix entries.
#
#    integer ROWIND(NZ_NUM), the row indices.
#
#    integer COLPTR(N+1), the column pointers.
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#
  n = len ( colptr ) - 1
  nz_num = len ( rowind )
#
#  Write the column information.
#
  filename = prefix + '_col.txt'
  output_unit = open ( filename, 'w' )

  for k in range ( 0, n + 1 ):
    s = '%d\n' % ( colptr[k] )
    output_unit.write ( s )

  output_unit.close ( )
#
#  Write the row information.
#
  filename = prefix + '_row.txt'
  output_unit = open ( filename, 'w' )

  for k in range ( 0, nz_num ):
    s = '%d\n' % ( rowind[k] )
    output_unit.write ( s )

  output_unit.close ( )
#
#  Write the value information.
#
  filename = prefix + '_val.txt'
  output_unit = open ( filename, 'w' )

  for k in range ( 0, nz_num ):
    s = '%d\n' % ( a[k] )
    output_unit.write ( s )

  output_unit.close ( )

  return

def ge_to_ccs ( Age ):

#*****************************************************************************80
#
## ge_to_ccs() converts a GE matrix to CCS format.
#
#  Discussion:
#
#    CCS is the compressed column storage format.
#
#    Associated with this format, we have an M by N matrix
#    with NZ_NUM nonzero entries.  We construct the column pointer
#    vector COL of length N+1, such that entries of column J will be
#    stored in positions COL(J) through COL(J+1)-1.  This indexing
#    refers to both the ROW and A vectors, which store the row indices
#    and the values of the nonzero entries.  The entries of the
#    ROW vector corresponding to each column are assumed to be
#    ascending sorted.
#
#    The CCS format is equivalent to the MATLAB "sparse" format,
#    and the Harwell Boeing "real unsymmetric assembled" (RUA) format.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Iain Duff, Roger Grimes, John Lewis,
#    User's Guide for the Harwell-Boeing Sparse Matrix Collection,
#    October 1992
#
#  Input:
#
#    real Age(M,N), the GE matrix.
#
#  Output:
#
#    integer COLPTR(N+1), points to the first element of each column.
#
#    integer ROWIND(NZ_NUM), contains the row indices of the elements.
#
#    real Accs(NZ_NUM), the CCS matrix.
#
  import numpy as np

  m, n = Age.shape
  nz_num = np.count_nonzero ( Age )
  colptr = np.zeros ( n + 1, dtype = int )
  rowind = np.zeros ( nz_num, dtype = int )
  value = np.zeros ( nz_num, dtype = float )
  
  k = 0
  colptr[0] = 0
  for j in range ( 0, n ):
    colptr[j+1] = colptr[j]
    for i in range ( 0, m ):
      if ( Age[i,j] != 0.0 ):
        value[k] = Age[i,j]
        rowind[k] = i
        colptr[j+1] = colptr[j+1] + 1
        k = k + 1;

  return rowind, colptr, value

def ge_to_ccs_risk ( ):

#*****************************************************************************80
#
## ge_to_ccs_risk() converts the RISK matrix from GE to CCS format.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ge_to_ccs_risk():' )
  print ( '  Convert Risk data from GE to CCS format.' )
#
#  Read GE data.
#
  prefix = 'risk'
  filename = prefix + '_ge.txt'
  Age = np.loadtxt ( filename ) 
#
#  Convert from GE to CCS format.
#
  row, col, val = ge_to_ccs ( Age )
#
#  Write the CCS data to files.
#
  ccs_write ( prefix, row, col, val )

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
  ge_to_ccs_test ( )
  timestamp ( )

