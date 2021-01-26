#! /usr/bin/env python
#
def plu ( n, pivot ):

#*****************************************************************************80
#
## PLU returns a matrix with known P, L and U factors.
#
#  Example:
#
#    Input:
#
#      N = 5
#      PIVOT = ( 1, 3, 3, 5, 5 )
#
#    Output:
#
#      A:
#
#         11            12           13            14           15
#          1.375         9.75        43.25         44.75        46.25
#          2.75         25           26.25         27.5         28.75
#          0.34375       2.4375       7.71875      17.625       73.125
#          0.6875        4.875       15.4375       60           61.5625
#
#      P:
#
#          1             0            0             0            0
#          0             0            1             0            0
#          0             1            0             0            0
#          0             0            0             0            1
#          0             0            0             1            0
#
#      L:
#
#         1              0            0             0            0
#         0.25           1            0             0            0
#         0.125          0.375        1             0            0
#         0.0625         0.1875       0.3125        1            0
#         0.03125        0.09375      0.15625       0.21875      1
#
#      U:
#
#        11             12           13            14           15
#         0             22           23            24           25
#         0              0           33            34           35
#         0              0            0            44           45
#         0              0            0             0           55
#
#  Note:
#
#    The LINPACK routine DGEFA will factor the above A as:
#
#       11             12             13             14             15
#      -0.125          22             23             24             25
#      -0.25           -0.375         33             34             35
#      -0.03125        -0.09375       -0.15625       44             45
#      -0.0625         -0.1875        -0.3125        -0.21875       55
#
#    and the pivot information in the vector IPVT as:
#
#      ( 1, 3, 3, 5, 5 ).
#
#    The LAPACK routine DGETRF will factor the above A as:
#
#      11              12             13             14             15
#      0.25            22             23             24             25
#      0.125            0.375         33             34             35
#      0.0625           0.1875         0.3125        44             45
#      0.03125          0.09375        0.15625        0.21875       55
#
#   and the pivot information in the vector IPIV as:
#
#     ( 1, 3, 3, 5, 5 ).
#
#  Method:
#
#    The L factor will have unit diagonal, and subdiagonal entries
#    L(I,J) = ( 2 * J - 1 ) / 2^I, which should result in a unique
#    value for every entry.
#
#    The U factor of A will have entries
#    U(I,J) = 10 * I + J, which should result in "nice" entries as long
#    as N < 10.
#
#    The P factor can be deduced by applying the pivoting operations
#    specified by PIVOT in reverse order to the rows of the identity.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer PIVOT(N), the list of pivot rows.  PIVOT(I)
#    must be a value between I and N, reflecting the choice of
#    pivot row on the I-th step.  For no pivoting, set PIVOT(I) = I.
#
#    Output, real P(N,N), L(N,N), U(N,N), the P, L and U factors
#    of A, as defined by Gaussian elimination with partial pivoting.
#    P is a permutation matrix, L is unit lower triangular, and U
#    is upper trianguler.
#
#    Output, real A(N,N), the matrix.
#
  from r8mat_mm import r8mat_mm

  p, l, u = plu_plu ( n, pivot )

  lu = r8mat_mm ( n, n, n, l, u )
  a = r8mat_mm ( n, n, n, p, lu )

  return a

def plu_determinant ( n, pivot ):

#*****************************************************************************80
#
## PLU_DETERMINANT returns the determinant of the PLU matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer PIVOT(N), the list of pivot rows.  PIVOT(I)
#    must be a value between I and N, reflecting the choice of
#    pivot row on the I-th step.  For no pivoting, set PIVOT(I) = I.
#
#    Output, real VALUE, the determinant.
#
  from sys import exit

  p, l, u = plu_plu ( n, pivot )

  value = 1.0
  for i in range ( 0, n ):
    value = value * u[i,i]

  for i in range ( 0, n ):

    found = False
    for i2 in range ( i, n ):

      if ( p[i2,i] == 1.0 ):
        found = True
        if ( i2 != i ):
          for j in range ( 0, n ):
            t       = p[i2,j]
            p[i2,j] = p[i,j]
            p[i,j]  = t
          value = - value

    if ( not found ):
      print ( '' )
      print ( 'PLU_DETERMINANT - Fatal error!' )
      print ( '  Permutation matrix is illegal.' )
      exit ( 'PLU_DETERMINANT - Fatal error!' )

  return value

def plu_inverse ( n, pivot ):

#*****************************************************************************80
#
## PLU_INVERSE returns the inverse of a PLU matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer PIVOT(N), the list of pivot rows.  PIVOT(I)
#    must be a value between I and N, reflecting the choice of
#    pivot row on the I-th step.  For no pivoting, set PIVOT(I) = I.
#
#    Output, real A(N,N), the inverse matrix.
#
  import numpy as np
  from r8mat_mm import r8mat_mm
  from tri_l1_inverse import tri_l1_inverse
  from tri_u_inverse import tri_u_inverse

  p, l, u = plu_plu ( n, pivot )

  p_inverse = np.transpose ( p )

  l_inverse = tri_l1_inverse ( n, l )

  u_inverse = tri_u_inverse ( n, u )

  lipi = r8mat_mm ( n, n, n, l_inverse, p_inverse )
  
  a = r8mat_mm ( n, n, n, u_inverse, lipi )

  return a

def plu_plu ( n, pivot ):

#*****************************************************************************80
#
## PLU_PLU returns the PLU factors of the PLU matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer PIVOT(N), the list of pivot rows.  PIVOT(I)
#    must be a value between I and N, reflecting the choice of
#    pivot row on the I-th step.  For no pivoting, set PIVOT(I) = I.
#
#    Output, real P(N,N), L(N,N), U(N,N), the P, L and U factors.
#
  import numpy as np
  from sys import exit
#
#  Check that the pivot vector is legal.
#
  for i in range ( 0, n ):

    if ( pivot[i] < i or n - 1 < pivot[i] ):
      print ( '' )
      print ( 'PLU - Fatal error!' )
      print ( '  PIVOT[%d] = %d' % ( i, pivot[i] ) )
      print ( '  but must be between %d and %d.' % ( i, n - 1 ) )
      exit ( 'PLU - Fatal error!' )
#
#  Compute U.
#
  u = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        u[i,j] = float ( 10 * (  i + 1 ) + ( j + 1 ) )
#
#  Compute L.
#
  l = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      l[i,j] = float ( 2 * j + 1 ) / float ( 2 ** ( i + 1 ) )
    l[i,i] = 1.0
#
#  Compute P.
#
  p = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    p[i,i] = 1.0

  for i in range ( n - 1, -1, -1 ):
    k = pivot[i]
    if ( k != i ):
      for j in range ( 0, n ):
        t      = p[i,j]
        p[i,j] = p[k,j]
        p[k,j] = t

  return p, l, u

def plu_test ( ):

#*****************************************************************************80
#
## PLU_TEST tests PLU.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4_uniform_ab import i4_uniform_ab
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'PLU_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PLU computes the PLU matrix.' )

  m = 5
  n = m

  pivot = np.zeros ( n, dtype = np.int32 )
  seed = 123456789
  for i in range ( 0, n ):
    i4_lo = i
    i4_hi = n - 1
    pivot[i], seed = i4_uniform_ab ( i4_lo, i4_hi, seed )

  a = plu ( n, pivot )

  r8mat_print ( m, n, a, '  PLU matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PLU_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  plu_test ( )
  timestamp ( )
