#! /usr/bin/env python3
#
def divdif_test ( ):

#*****************************************************************************80
#
## divdif_test() tests divdif().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'divdif_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test divdif()' )

  cheby_t_zero_test ( )
  cheby_u_zero_test ( )
  data_to_dif_test ( )
  data_to_dif_display_test ( )
  data_to_r8poly_test ( )
  data_to_table_test ( )
  dif_antideriv_test ( )
  dif_append_test ( )
  dif_basis_test ( )
  dif_basis_deriv_test ( )
  dif_basis_derivk_test ( )
  dif_deriv_test ( )
  dif_derivk_table_test ( )
  dif_print_test ( )
  dif_shift_zero_test ( )
  dif_to_r8poly_test ( )
  dif_value_test ( )
  lagrange_rule_test ( )
  lagrange_sum_test ( )
  lagrange_value_test ( )
  ncc_rule_test ( )
  nco_rule_test ( )
  r8mat_print_test ( )
  r8mat_transpose_print_test ( )
  r8poly_ant_coef_test ( )
  r8poly_ant_value_test ( )
  r8poly_basis_test ( )
  r8poly_deriv_coef_test ( )
  r8poly_deriv_value_test ( )
  r8poly_print_test ( )
  r8poly_shift_test ( )
  r8poly_value_horner_test ( )
  r8vec_indicator1_test ( )
  r8vec_is_distinct_test ( )
  roots_to_dif_test ( )
  roots_to_r8poly_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'divdif_test():' )
  print ( '  Normal end of execution.' )

  return

def cheby_t_zero ( n ):

#*****************************************************************************80
#
## cheby_t_zero() returns zeroes of the Chebyshev polynomial T(n,x).
#
#  Discussion:
#
#    The I-th zero is cos((2*I-1)*PI/(2*N)), I = 1 to N
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#  Output:
#
#    real Z(N), the zeroes.
#
  import numpy as np

  z = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( 2 * i + 1 ) * np.pi / float ( 2 * n )
    z[i] = np.cos ( angle )

  return z

def cheby_t_zero_test ( ):

#*****************************************************************************80
#
## cheby_t_zero_test() tests cheby_t_zero().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'cheby_t_zero_test():' )
  print ( '  cheby_t_zero() computes the zeros of T(n,x);' )
  print ( '' )
  print ( '     N      X' )

  for n in range ( 1, 6 ):

    x = cheby_t_zero ( n )

    print ( '' )
    for i in range ( 0, n ):
      print ( '  %4d  %8.4f' % ( i, x[i] ) )

  return

def cheby_u_zero ( n ):

#*****************************************************************************80
#
## cheby_u_zero() returns zeroes of the Chebyshev polynomial U(n,x).
#
#  Discussion:
#
#    The I-th zero of U(n,x) is cos((I-1)*PI/(N-1)), I = 1 to N
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#  Output:
#
#    real Z(N), the zeroes.
#
  import numpy as np

  z = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( n + 1 )
    z[i] = np.cos ( angle )

  return z

def cheby_u_zero_test ( ):

#*****************************************************************************80
#
## cheby_u_zero_test() tests cheby_u_zero().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'cheby_u_zero_test():' )
  print ( '  cheby_u_zero() computes the zeros of U(n,x);' )
  print ( '' )
  print ( '     N      X' )

  for n in range ( 1, 6 ):

    x = cheby_u_zero ( n )

    print ( '' )
    for i in range ( 0, n ):
      print ( '  %4d  %8.4f' % ( i, x[i] ) )

  return

def data_to_dif ( ntab, xtab, ytab ):

#*****************************************************************************80
#
## data_to_dif() computes a divided difference table from raw data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carl deBoor,
#    A Practical Guide to Splines,
#    Springer, 2001,
#    ISBN: 0387953663,
#    LC: QA1.A647.v27.
#
#  Input:
#
#    integer NTAB, the number of pairs of points
#    (XTAB(I),YTAB(I)) which are to be used as data.  The
#    number of entries to be used in DIFTAB, XTAB and YTAB.
#
#    real XTAB(NTAB), the X values at which data was taken.
#
#    real YTAB(NTAB), the corresponding Y values.
#
#  Output:
#
#    real DIFTAB(NTAB), the divided difference
#    coefficients corresponding to the input (XTAB,YTAB).
#
  if ( not r8vec_is_distinct ( ntab, xtab ) ):
    print ( '' )
    print ( 'data_to_dif(): Fatal error!' )
    print ( '  Two entries of XTAB are equal!' )
    print ( xtab )
    raise Exception ( 'data_to_dif(): Fatal error!' )
#
#  Copy the data values into DIFTAB.
#
  diftab = ytab.copy()
#
#  Compute the divided differences.
#
  for i in range ( 2, ntab + 1 ):
    for j in range ( ntab, i - 1, -1 ):
      diftab[j-1] = ( diftab[j-1] - diftab[j-1-1] ) / ( xtab[j-1] - xtab[j+1-i-1] )

  return diftab

def data_to_dif_test ( ):

#*****************************************************************************80
#
## data_to_dif_test() tests data_to_dif().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'data_to_dif_test():' )
  print ( '  data_to_dif() computes the Newton polynomial coefficients' )
  print ( '  for a divided difference interpolant, from data' )
#
#  Set XTAB, YTAB to X, exp(x).
#
  ntab = 4
  xtab = np.arange ( ntab ) + 1.0
  ytab = np.exp ( xtab )

  r8vec2_print ( xtab, ytab, '  The data to be processed:' )

  diftab = data_to_dif ( ntab, xtab, ytab )

  dif_print ( ntab, xtab, diftab, '  The divided difference polynomial:' )

  return

def data_to_dif_display ( ntab, xtab, ytab ):

#*****************************************************************************80
#
## data_to_dif_display() computes a divided difference table and shows how.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 September 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NTAB, the number of pairs of points
#    (XTAB(I),YTAB(I)) which are to be used as data.  The
#    number of entries to be used in DIFTAB, XTAB and YTAB.
#
#    real XTAB(NTAB), the X values at which data was taken.
#
#    real YTAB(NTAB), the corresponding Y values.
#
#  Output:
#
#    real DIFTAB(NTAB), the divided difference
#    coefficients corresponding to the input (XTAB,YTAB).
#
  if ( not r8vec_is_distinct ( ntab, xtab ) ):
    print ( '' )
    print ( 'data_to_dif_display(): Fatal error!' )
    print ( '  Two entries of XTAB are equal!' )
    raise Exception ( 'data_to_dif_display(): Fatal error!' )

  print ( '' )
  print ( 'Divided difference table:' )
  print ( '' )
  print ( '    ', end = '' )
  for i in range ( 0, ntab ):
    print ( '%14f' % ( xtab[i] ), end = '' )
  print ( '' )
  print ( '' )
  print ( '  0 ', end = '' )
  for i in range ( 0, ntab ):
    print ( '%14f' % ( ytab[i] ), end = '' )
  print ( '' )
#
#  Copy the data values into DIFTAB.
#
  diftab = ytab.copy()
#
#  Compute the divided differences.
#
  for i in range ( 2, ntab + 1 ):
    for j in range ( ntab, i - 1, -1 ):
      diftab[j-1] = ( diftab[j-1] - diftab[j-1-1] ) / ( xtab[j-1] - xtab[j+1-i-1] )

    print ( '%3d ' % ( i - 1 ), end = '' )
    for j in range ( i, ntab + 1 ):
      print ( '%14f' % ( diftab[j-1] ), end = '' )
    print ( '' )

  return diftab

def data_to_dif_display_test ( ):

#*****************************************************************************80
#
## data_to_dif_display_test() tests data_to_dif_display().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'data_to_dif_display_test():' )
  print ( '  data_to_dif_display() sets up a difference table' )
  print ( '  and displays intermediate calculations' )
#
#  Set XTAB, YTAB to X, exp(x).
#
  ntab = 4
  xtab = np.arange ( ntab ) + 1.0
  ytab = np.exp ( xtab )

  r8vec2_print ( xtab, ytab, '  The data to be processed:' )

  diftab = data_to_dif_display ( ntab, xtab, ytab )

  dif_print ( ntab, xtab, diftab, '  The divided difference polynomial:' )

  return

def data_to_r8poly ( ntab, xtab, ytab ):

#*****************************************************************************80
#
## data_to_r8poly() computes the coefficients of a polynomial interpolating data.
#
#  Discussion:
#
#    Space can be saved by using a single array for both the C and
#    YTAB parameters.  In that case, the coefficients will
#    overwrite the Y data without interfering with the computation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carl deBoor,
#    A Practical Guide to Splines,
#    Springer, 2001,
#    ISBN: 0387953663,
#    LC: QA1.A647.v27.
#
#  Input:
#
#    integer NTAB, the number of data points.
#
#    real XTAB(NTAB), YTAB(NTAB), the data values.
#
#  Output:
#
#    real C(NTAB), the coefficients of the
#    polynomial that passes through the data (XTAB,YTAB).  C(1) is the
#    constant term.
#
  if ( not r8vec_is_distinct ( ntab, xtab ) ):
    print ( '' )
    print ( 'data_to_r8poly(): Fatal error!' )
    print ( '  Two entries of XTAB are equal!' )
    raise Exception ( 'data_to_r8poly(): Fatal error!' )

  diftab = data_to_dif ( ntab, xtab, ytab )

  c = dif_to_r8poly ( ntab, xtab, diftab )

  return c

def data_to_r8poly_test ( ):

#*****************************************************************************80
#
## data_to_r8poly_test() tests data_to_r8poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'data_to_r8poly_test():' )
  print ( '  data_to_r8poly() computes the standard polynomial' )
  print ( '  coefficients for an interpolant, from data' )
#
#  Set XTAB, YTAB to X, exp(x).
#
  n = 4
  x = np.arange ( n ) + 1.0
  y = np.exp ( x )
  r8vec2_print ( x, y, '  The data to be processed:' )

  c = data_to_r8poly ( n, x, y )
  r8poly_print ( c, '  The interpolating polynomial:' )

  return

def data_to_table ( x, y ):

#*****************************************************************************80
#
## data_to_table() computes a divided difference table from raw data.
#
#  Discussion:
#
#    The full triangular table is computed and returned.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carl deBoor,
#    A Practical Guide to Splines,
#    Springer, 2001,
#    ISBN: 0387953663,
#    LC: QA1.A647.v27.
#
#  Input:
#
#    real x(n), y(n): the pairs of data.
#
#  Output:
#
#    real t(n,n): the full divided difference table.  
#    The usual divided difference vector is in the first row.
#
  import numpy as np

  n = x.shape[0]

  t = np.zeros ( [ n, n ] )
#
#  Column 1 is the y data.
#
  t[:,0] = y.copy()
#
#  Compute columns 2 through n.
#
  for j in range ( 2, n + 1 ):
    for i in range ( 1, n + 2 - j ):
      t[i-1,j-1] = ( t[i+1-1,j-1-1] - t[i-1,j-1-1] ) / ( x[i+j-1-1] - x[i-1] )

  return t

def data_to_table_test ( ):

#*****************************************************************************80
#
## data_to_table_test() tests data_to_table().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'data_to_table_test():' )
  print ( '  data_to_table() computes the full divided difference' )
  print ( '  table for a given set of data.' )
  print ( '  The usual divided difference vector is the first row.' )

  n = 4
  x = np.linspace ( 0.0, n - 1, n )
  y = x**3

  r8vec2_print ( x, y, '  Data to be processed:' )

  t = data_to_table ( x, y )

  r8mat_print ( n, n, t, '  Divided difference table:' )

  return

def dif_antideriv ( ntab, xtab, diftab ):

#*****************************************************************************80
#
## dif_antideriv() computes the antiderivative of a divided difference polynomial.
#
#  Discussion:
#
#    The routine uses the divided difference representation
#    of a polynomial to compute the divided difference representation
#    of the antiderivative of the polynomial.
#
#    The antiderivative of a polynomial P(X) is any polynomial Q(X)
#    with the property that d/dX Q(X) = P(X).
#
#    This routine chooses the antiderivative whose constant term is zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NTAB, the size of the difference table.
#
#    real XTAB(NTAB), the abscissas of the difference table.
#
#    real DIFTAB(NTAB), the difference table.
#
#  Output:
#
#    integer NTAB2, the size of the difference table for the
#    antiderivative, which will be NTAB+1.
#
#    real XTAB2(NTAB2), the abscissas of the
#    difference table for the antiderivative.
#
#    real DIFTAB2(NTAB2), the difference table
#    for the antiderivative.
#
  import numpy as np
#
#  Copy the input data.
#
  xtab1 = xtab.copy()
  diftab1 = diftab.copy()
#
#   Shift the abscissas to zero.
#
  xtab1, diftab1 = dif_shift_zero ( ntab, xtab1, diftab1 )
#
#  Append a final zero to XTAB.
#
  ntab2 = ntab + 1
  xtab2 = np.zeros ( ntab2 )
#
#  Get the antiderivative of the standard form polynomial.
#
  d = ntab - 1
  diftab2 = r8poly_ant_coef ( d, diftab1 )

  return ntab2, xtab2, diftab2

def dif_antideriv_test ( ):

#*****************************************************************************80
#
## dif_antideriv_test() tests dif_antideriv()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'dif_antideriv_test()' )
  print ( '  dif_antideriv() computes the difference form of the antiderivative' )
#
#  Set XTAB, YTAB to X, X^3 + 2x^2 + 3x + 4.
#
  ntab = 4
  xtab = np.arange ( ntab )
  ytab = xtab**3 + 2.0 * xtab**2 + 3.0 * xtab + 4.0

  ydif = data_to_dif_display ( ntab, xtab, ytab )
  dif_print ( ntab, xtab, ydif, '  The divided difference polynomial:' )
#
#  Compute a table for the antiderivative.
#
  ntab2, xtab2, ydif2 = dif_antideriv ( ntab, xtab, ydif )

  dif_print ( ntab2, xtab2, ydif2, '  The antiderivative:' )

  return

def dif_append ( xtab, diftab, xval, yval ):

#*****************************************************************************80
#
## dif_append() adds a pair of data values to a divided difference table.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real XTAB(NTAB), the abscissas of the table.
#
#    real DIFTAB(NTAB), the difference table.
#
#    real XVAL, the X data value to be inserted as XTAB(1).
#
#    real YVAL, the Y data value to be inserted as YTAB(1).
#
#  Output:
#
#    real XTAB2(NTAB+1), the updated abscissas.
#
#    real DIFTAB2(NTAB+1), the updated difference table.
#
  import numpy as np

  ntab = xtab.shape[0]
#
#  Move the original data up one index and insert the new data.
#
  ntab2 = ntab + 1
  xtab2 = np.zeros ( ntab2 )
  diftab2 = np.zeros ( ntab2 )

  diftab2[1:ntab2] = diftab[0:ntab]
  diftab2[0] = yval

  xtab2[1:ntab2] = xtab[0:ntab]
  xtab2[0] = xval
#
#  Recompute the difference table.
#
  for i in range ( 1, ntab2 ):
    diftab2[i] = ( diftab2[i] - diftab2[i-1] ) / ( xtab2[i] - xtab2[0] )

  return xtab2, diftab2

def dif_append_test ( ):

#*****************************************************************************80
#
## dif_append_test() tests dif_append().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'dif_append_test():' )
  print ( '  dif_append() updates a divided difference polynomial' )
  print ( '  to include a new data item' )
#
#  Set XTAB, YTAB to X, exp(x).
#
  ntab = 4
  xtab = np.arange ( ntab ) + 1.0
  ytab = np.exp ( xtab )

  diftab = data_to_dif ( ntab, xtab, ytab )

  dif_print ( ntab, xtab, diftab, '  The divided difference polynomial:' )
#
#  Append (5,25) to the table.
#
  print ( '' )
  print ( '  Append the data (5,exp(5)) to the table.' )

  xval = ntab + 1
  yval = np.exp ( xval )

  xtab, diftab = dif_append ( xtab, diftab, xval, yval )
  ntab = ntab + 1

  dif_print ( ntab, xtab, diftab, \
    '  The augmented divided difference polynomial:' )

  return

def dif_basis ( ntab, xtab ):

#*****************************************************************************80
#
## dif_basis() computes all Lagrange basis polynomials in divided difference form.
#
#  Discussion:
#
#    The I-th Lagrange basis polynomial for a set of NTAB X values XTAB,
#    L(I,NTAB,XTAB)(X) is a polynomial of order NTAB-1 which is zero at
#    XTAB(J) for J not equal to I, and 1 when J is equal to I.
#
#    The Lagrange basis polynomials have the property that the interpolating
#    polynomial through a set of NTAB data points (XTAB,YTAB) may be
#    represented as
#
#      P(X) = Sum ( 1 <= I <= N ) YTAB(I) * L(I,NTAB,XTAB)(X)
#
#    Higher order interpolation at selected points may be accomplished
#    using repeated X values, and scaled derivative values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carl deBoor,
#    A Practical Guide to Splines,
#    Springer, 2001,
#    ISBN: 0387953663,
#    LC: QA1.A647.v27.
#
#  Input:
#
#    integer NTAB, the number of X data points XTAB, and the number of
#    basis polynomials to compute.
#
#    real XTAB(NTAB), the X values upon which the
#    Lagrange basis polynomials are to be based.
#
#  Output:
#
#    real DIFTAB(NTAB,NTAB), the set of divided
#    difference tables.  Column I of DIFTAB contains the table for
#    the I-th Lagrange basis polynomial.
#
  import numpy as np
#
#  Initialize DIFTAB to the identity matrix.
#
  diftab = np.zeros ( [ ntab, ntab ] )

  for i in range ( 0, ntab ):
    diftab[i,i] = 1.0
#
#  Compute each Lagrange basis polynomial.
#
  for i in range ( 0, ntab ):
    diftab[:,i] = data_to_dif ( ntab, xtab, diftab[:,i] ) 

  return diftab

def dif_basis_test ( ):

#*****************************************************************************80
#
## dif_basis_test() tests dif_basis().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  ntab = 5
  nstep = 9

  print ( '' )
  print ( 'dif_basis_test():' )
  print ( '  dif_basis() computes Lagrange basis polynomials' )
  print ( '  in difference form.' )
#
#  Set the base points.
#
  xtab = np.arange ( ntab ) + 1.0

  r8vec_print ( ntab, xtab, '  The base points:' )
#
#  Get the difference tables for the basis polynomials and print them.
#
  diftab = dif_basis ( ntab, xtab )

  print ( '' )
  print ( '  The table of difference vectors defining the basis' )
  print ( '  polynomials.  Each column represents a polynomial.' )
  print ( '' )
  for i in range ( 0, ntab ):
    print ( '  ', end = '' )
    for j in range ( 0, ntab ):
      print ( '%14f' % ( diftab[i,j] ), end = '' )
    print ( '' )
#
#  Evaluate basis polynomial 3 at a set of points.
#
  print ( '' )
  print ( '  Evaluate basis polynomial #2 at a set of points.' )
  print ( '' )
  print ( '      X        Y' )
  print ( '' )
  xhi = ntab
  xlo = 1.0

  for i in range ( 0, nstep ):

    xval = ( ( nstep - i - 1 ) * xlo   \
           + (         i     ) * xhi ) \
           / ( nstep     - 1 )

    yval = dif_value ( ntab, xtab, diftab[:,2], xval )

    print ( '  %14f  %14f' % ( xval, yval ) )

  return

def dif_basis_deriv ( nd, xd ):

#*****************************************************************************80
#
## dif_basis_deriv(): Lagrange basis derivative difference tables.
#
#  Discussion:
#
#    Given ND points XD, a Lagrange basis polynomial L(J)(X) is associated
#    with each point XD(J).
#
#    This function computes a table DDP(*,*) whose J-th column contains
#    the difference table for the first derivative of L(J)(X).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carl deBoor,
#    A Practical Guide to Splines,
#    Springer, 2001,
#    ISBN: 0387953663,
#    LC: QA1.A647.v27.
#
#  Input:
#
#    integer ND, the number of data points.
#
#    real XD(ND), the X values upon which the 
#    Lagrange basis polynomials are to be based.
#
#  Output:
#
#    real XDP(ND-1), the X values upon with
#    the derivative difference table is based.  In fact, these are
#    all 0.
#
#    real DDP(ND-1,ND), the divided difference 
#    tables for all the Lagrange basis polynomials.  Column J of DDP
#    contains the table for basis polynomial associated with XD(J).
#
  import numpy as np

  ddp = np.zeros ( [ nd - 1, nd ] )
#
#  Process the vectors one column at a time.
#
  for j in range ( 0, nd ):
#
#  Set the data.
#
    yd = np.zeros ( nd )
    yd[j] = 1.0
#
#  Compute the divided difference table.
#
    dd = data_to_dif ( nd, xd, yd )
#
#  Compute the divided difference table for the derivative.
#
    ndp, xdp, ddp[:,j] = dif_deriv ( nd, xd, dd )

  return xdp, ddp

def dif_basis_deriv_test ( ):

#*****************************************************************************80
#
## dif_basis_deriv_test() tests dif_basis_deriv()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nd = 3
  xd = np.array ( [ -2.0, 1.0, 5.0 ] )

  print ( '' )
  print ( 'dif_basis_deriv_test():' )
  print ( '  dif_basis_deriv() computes difference tables for' )
  print ( '  the first derivative of each Lagrange basis.' )
  
  xdp, ddp = dif_basis_deriv ( nd, xd )
#
#  Because the difference tables were shifted to all 0 abscissas,
#  they contain the polynomial coefficients.
#
  r8mat_transpose_print ( nd - 1, nd, ddp, \
    '  Lagrange basis derivative polynomial coefficients:' )

  c = dif_to_r8poly ( nd - 1, xdp, ddp[:,0] )
  r8poly_print ( c, '  P1''=-(2x-6)/21' )

  c = dif_to_r8poly ( nd - 1, xdp, ddp[:,1] )
  r8poly_print ( c, '  P2''=-(2x-3)/12' )

  c = dif_to_r8poly ( nd - 1, xdp, ddp[:,2] )
  r8poly_print ( c, '  P3''=(2x+1)/28' )

  return

def dif_basis_derivk ( nd, xd, k ):

#*****************************************************************************80
#
## dif_basis_derivk(): Lagrange basis K-th derivative difference tables.
#
#  Discussion:
#
#    Given ND points XD, a Lagrange basis polynomial L(J)(X) is associated
#    with each point XD(J).
#
#    This function computes a table DDP(*,*) whose J-th column contains
#    the difference table for the K-th derivative of L(J)(X).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carl deBoor,
#    A Practical Guide to Splines,
#    Springer, 2001,
#    ISBN: 0387953663,
#    LC: QA1.A647.v27.
#
#  Input:
#
#    integer ND, the number of data points.
#
#    real XD(ND), the X values upon which the 
#    Lagrange basis polynomials are to be based.
#
#    integer K, the index of the derivative.
#
#  Output:
#
#    real XDP(ND-K), the X values upon with
#    the derivative difference table is based.  In fact, these are
#    all 0.
#
#    real DDP(ND-K,ND), the divided difference 
#    tables for all the Lagrange basis polynomials.  Column J of DDP
#    contains the table for basis polynomial associated with XD(J).
#
  import numpy as np

  ddp = np.zeros ( [ nd - k, nd ] )
#
#  Process the vectors one column at a time.
#
  for j in range ( 0, nd ):
#
#  Set the data.
#
    yd = np.zeros ( nd )
    yd[j] = 1.0
#
#  Compute the divided difference table.
#
    dd = data_to_dif ( nd, xd, yd )
#
#  Compute the divided difference table for the derivative.
#
    xdp, ddp[0:nd-k,j] = dif_derivk_table ( nd, xd, dd, k )

  return xdp, ddp

def dif_basis_derivk_test ( ):

#*****************************************************************************80
#
## dif_basis_derivk_test() tests dif_basis_derivk()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nd = 5
  k = 2
  xd = np.array ( [ 1.0, 2.0, 3.0, 4.0, 5.0 ] )

  print ( '' )
  print ( 'dif_basis_derivk_test():' )
  print ( '  dif_basis_derivk() computes difference tables for' )
  print ( '  the K-th derivative of each Lagrange basis.' )
  
  xdp, ddp = dif_basis_derivk ( nd, xd, k )
#
#  Because the difference tables were shifted to all 0 abscissas,
#  they contain the polynomial coefficients.
#
  r8mat_transpose_print ( nd - k, nd, ddp, \
    '  Lagrange basis K-derivative polynomial coefficients:' )

  c = dif_to_r8poly ( nd - k, xdp, ddp[0:nd-k,0] )
  d = nd - k - 1
  r8poly_print ( c, '  P0\'=(12x^2-84x+142)/24' )

  c = dif_to_r8poly ( nd - k, xdp, ddp[0:nd-k,1] )
  r8poly_print ( c, '  P1\'=-2x^2+13x-59/3' )

  c = dif_to_r8poly ( nd - k, xdp, ddp[0:nd-k,2] )
  r8poly_print ( c, '  P2\'=3x^2-18x+49/2' )

  c = dif_to_r8poly ( nd - k, xdp, ddp[0:nd-k,3] )
  r8poly_print ( c, '  P3\'=-2x^2+11x-41/3' )

  c = dif_to_r8poly ( nd - k, xdp, ddp[0:nd-k,4] )
  r8poly_print ( c, '  P4\'=(6x^2-30x+35)/12' )

  return

def dif_basis_i ( ival, ntab, xtab ):

#*****************************************************************************80
#
## dif_basis_i() computes the I-th Lagrange basis polynomial in divided difference form.
#
#  Discussion:
#
#    The I-th Lagrange basis polynomial for a set of NTAB X values XTAB,
#    L(I,NTAB,XTAB)(X) is a polynomial of order NTAB-1 which is zero at
#    XTAB(J) for J not equal to I, and 1 when J is equal to I.
#
#    The Lagrange basis polynomials have the property that the interpolating
#    polynomial through a set of NTAB data points (XTAB,YTAB) may be
#    represented as
#
#      P(X) = Sum ( 1 <= I <= N ) YTAB(I) * L(I,NTAB,XTAB)(X)
#
#    Higher order interpolation at selected points may be accomplished
#    using repeated X values, and scaled derivative values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carl deBoor,
#    A Practical Guide to Splines,
#    Springer, 2001,
#    ISBN: 0387953663,
#    LC: QA1.A647.v27.
#
#  Input:
#
#    integer IVAL, the index of the desired Lagrange basis polynomial.
#    IVAL should be between 0 and NTAB-1.
#
#    integer NTAB, the number of data points XTAB.
#
#    real XTAB(NTAB), the X values upon which the
#    Lagrange basis polynomial is to be based.
#
#  Output:
#
#    real DIFTAB(NTAB), the divided difference table
#    for the IVAL-th Lagrange basis polynomial.
#
  import numpy as np
#
#  Check IVAL.
#
  if ( ival < 0 or ntab - 1 < ival ):
    print ( '' )
    print ( 'dif_basis_i(): Fatal error!' )
    print ( '  IVAL must be between 1 and ', ntab )
    print ( '  but your value is ', ival )
    raise Exception ( 'dif_basis_i(): Fatal error!' )
#
#  Initialize DIFTAB to Delta(I,J).
#
  diftab = np.zeros ( ntab )
  diftab[ival] = 1.0
#
#  Compute the IVAL-th Lagrange basis polynomial.
#
  diftab = data_to_dif ( ntab, xtab, diftab )

  return diftab

def dif_deriv ( nd, xd, yd ):

#*****************************************************************************80
#
## dif_deriv() computes the derivative of a divided difference polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carl deBoor,
#    A Practical Guide to Splines,
#    Springer, 2001,
#    ISBN: 0387953663,
#    LC: QA1.A647.v27.
#
#  Input:
#
#    integer ND: the size of the input table.
#
#    real XD(ND): the abscissas for the divided
#    difference table.
#
#    real YD(ND): the divided difference table.
#
#  Output:
#
#    integer NDP: ND - 1.
#
#    real XDP(ND-1): the abscissas for the divided
#    difference table for the derivative.
#
#    real YDP(ND-1): the divided difference table for the derivative.
#
  import numpy as np
#
#  Shift the abscissas to zero.
#
  xd_shifted = xd.copy ( )
  yd_shifted = yd.copy ( )
  xd_shifted, yd_shifted = dif_shift_zero ( nd, xd_shifted, yd_shifted )
#
#  Construct the derivative.
#
  ndp = nd - 1

  xdp = np.zeros ( ndp )
  ydp = np.zeros ( ndp )

  for i in range ( 0, nd - 1 ):
    ydp[i] = ( i + 1 ) * yd_shifted[i+1]

  return ndp, xdp, ydp

def dif_deriv_test ( ):

#*****************************************************************************80
#
## dif_deriv_test() tests dif_deriv()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'dif_deriv_test():' )
  print ( '  dif_deriv() computes the difference form of the derivative' )
#
#  Set XTAB, YTAB to X, X^3 + 2x^2 + 3x + 4.
#
  ntab = 4
  xtab = np.arange ( ntab )
  ytab = xtab**3 + 2.0 * xtab**2 + 3.0 * xtab + 4.0

  ydif = data_to_dif_display ( ntab, xtab, ytab )
  dif_print ( ntab, xtab, ydif, '  The divided difference polynomial:' )
#
#  Compute a table for the derivative.
#
  ntab2, xtab2, ydif2 = dif_deriv ( ntab, xtab, ydif )

  dif_print ( ntab2, xtab2, ydif2, '  The derivative:' )

  return

def dif_derivk_table ( nd, xd, dd, k ):

#*****************************************************************************80
#
## dif_derivk_table() computes the divided difference table for K-th derivative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carl deBoor,
#    A Practical Guide to Splines,
#    Springer, 2001,
#    ISBN: 0387953663,
#    LC: QA1.A647.v27.
#
#  Input:
#
#    integer ND, the size of the input table.
#
#    real XD(ND), the abscissas for the divided
#    difference table.
#
#    real DD(ND), the divided difference table.
#
#    integer K, the index of the derivative.
#    0 <= K
#
#    real XDK(ND-K), the abscissas for the divided
#    difference table for the derivative.
#
#  Output:
#
#    real XDK(ND-K), the updated abscissas for the divided
#    difference table for the derivative.  (All zero!)
#
#    real DDK(ND-K), the divided difference 
#    table for the derivative.
#
  import numpy as np

  if ( k < 0 ):
    print ( '' )
    print ( 'dif_derivk_table(): Fatal error!' )
    print ( '  K < 0.' )
    raise Exception ( 'dif_derivk_table(): Fatal error!' )

  if ( nd <= k ):
    ndk = 0
    xdk = []
    ddk = []
    return xdk, ddk
#
#  Shift the abscissas to zero.
#
  ndk = nd

  xd_temp = xd.copy ( )
  dd_temp = dd.copy ( )

  xd_temp, dd_temp = dif_shift_zero ( nd, xd_temp, dd_temp )
#
#  Repeatedly differentiate.
#
  for j in range ( 0, k ):
 
    ndk = ndk - 1

    for i in range ( 0, ndk ):
      dd_temp[i] = ( i + 1 ) * dd_temp[i+1]

  ddk = dd_temp[0:ndk]
  xdk = np.zeros ( ndk )

  return xdk, ddk

def dif_derivk_table_test ( ):

#*****************************************************************************80
#
## dif_derivk_table_test() tests dif_derivk_table()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'dif_derivk_table_test():' )
  print ( '  dif_derivk_table() computes the K-th derivative' )
  print ( '  for a divided difference table.' )
#
#  Set the 0 data points.
#
  n0 = 5
  x0 = np.linspace ( -2.0, +2.0, 5 )
#
#  Set data for x^4/24+x^3/3+x^2/2+x+1
#
  f0 = np.ones ( n0 )
  for i in range ( 4, 0, -1 ):
    f0 = f0 * x0 / i + 1.0
#
#  Compute the difference table.
#
  d0 = data_to_dif ( n0, x0, f0 )
  dif_print ( n0, x0, d0, '  The divided difference polynomial P0:' )

  c0 = dif_to_r8poly ( n0, x0, d0 )
  d = n0 - 1
  r8poly_print ( c0, '  Using DIF_TO_R8POLY' )
#
#  Compute the difference table for the K=1 derivative.
#
  k = 1
  n1 = n0 - k
  x1, d1 = dif_derivk_table ( n0, x0, d0, k )
#
#  Compute the difference table for the K=2 derivative.
#
  k = 2
  n2 = n0 - k
  x2, d2 = dif_derivk_table ( n0, x0, d0, k )
#
#  Compute the difference table for the K=3 derivative.
#
  k = 3
  n3 = n0 - k
  x3, d3 = dif_derivk_table ( n0, x0, d0, k )
#
#  Compute the difference table for the K=4 derivative.
#
  k = 4
  n4 = n0 - k
  x4, d4 = dif_derivk_table ( n0, x0, d0, k )
#
#  Evaluate all 5 polynomials.
#
  print ( '' )
  print ( '  Evaluate difference tables for the function P0' )
  print ( '  and its first four derivatives, P1...P4.' )
  print ( '' )
  print ( '      X         P0        P1        P2        P3        P4' )
  print ( '' )

  for i in range ( 0, 11 ):
    x = i / 5.0
    y0 = dif_value ( n0, x0, d0, x )
    y1 = dif_value ( n1, x1, d1, x )
    y2 = dif_value ( n2, x2, d2, x )
    y3 = dif_value ( n3, x3, d3, x )
    y4 = dif_value ( n4, x4, d4, x )
    print ( '  %8.4f  %8.4f  %8.4f  %8.4f  %8.4f  %8.4f' \
      % ( x, y0, y1, y2, y3, y4 ) )

  return

def dif_print ( ntab, xtab, diftab, title ):

#*****************************************************************************80
#
## dif_print() prints the polynomial represented by a divided difference table.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NTAB, the dimension of the arrays DIFTAB and XTAB.
#
#    real XTAB(NTAB), the X values for the polynomial.
#
#    real DIFTAB(NTAB), the divided difference table
#    for the polynomial.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  print ( '  p(x) =                           %14.8f' % ( diftab[0] ) )

  for i in range ( 1, ntab ):
    print ( '       + ( x - %14.8f) * ( %14.8f' % ( xtab[i-1], diftab[i] ) )

  print ( '  ', end = '' )
  for i in range ( 0, ntab - 1 ):
    print ( ')', end = '' )
  print ( '' )

  return

def dif_print_test ( ):

#*****************************************************************************80
#
## dif_print_test() tests dif_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'dif_print_test():' )
  print ( '  dif_print() prints a Newton polynomial;' )
#
#  Set XTAB, YTAB to X, exp(x).
#
  ntab = 4
  xtab = np.arange ( ntab ) + 1.0
  ytab = np.exp ( xtab )

  r8vec2_print ( xtab, ytab, '  The data to be processed:' )

  diftab = data_to_dif ( ntab, xtab, ytab )

  dif_print ( ntab, xtab, diftab, '  The divided difference polynomial:' )

  return

def dif_shift_x ( nd, xd, yd, xv ):

#*****************************************************************************80
#
## dif_shift_x() replaces one abscissa of a divided difference table with a new one.
#
#  Discussion:
#
#    The routine shifts the representation of a divided difference polynomial by
#    dropping the last X value in XD, and adding a new X value to the
#    beginning of the XD array, suitably modifying the coefficients stored
#    in YD.
#
#    The representation of the polynomial is changed, but the polynomial itself
#    should be identical.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carl deBoor,
#    A Practical Guide to Splines,
#    Springer, 2001,
#    ISBN: 0387953663,
#    LC: QA1.A647.v27.
#
#  Input:
#
#    integer ND, the number of divided difference coefficients, and
#    the number of entries in XD.
#
#    real XD(ND), the abscissas for the divided difference table.
#
#    real YD(ND), the divided difference table.
#
#    real XV, a new X value which is to be used in
#    the representation of the polynomial.  On output, XD(1) equals
#    XV and the representation of the polynomial has been suitably changed.
#    Note that XV does not have to be distinct from any of the original XD
#    values.
#
#  Output:
#
#    real XD(ND), the updated abscissas.
#
#    real YD(ND), the updated divided difference table.
#

#
#  Recompute the divided difference coefficients.
#
  for i in range ( nd - 2, -1, -1 ):
    yd[i] = yd[i] + ( xv - xd[i] ) * yd[i+1]
#
#  Shift the XD values up one position and insert XV.
#
  xd[1:nd] = xd[0:nd-1]

  xd[0] = xv

  return xd, yd

def dif_shift_zero ( nd, xd, yd ):

#*****************************************************************************80
#
## dif_shift_zero() shifts a divided difference table so that all abscissas are zero.
#
#  Discussion:
#
#    When the abscissas are changed, the coefficients naturally
#    must also be changed.
#
#    The resulting pair (XD, YD) still represents the
#    same polynomial, but the entries in YD are now the
#    standard polynomial coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carl deBoor,
#    A Practical Guide to Splines,
#    Springer, 2001,
#    ISBN: 0387953663,
#    LC: QA1.A647.v27.
#
#  Input:
#
#    integer ND, the length of the XD and YD arrays.
#
#    real XD(ND), the abscissas of the difference table.
#
#    real YD(ND), the divided difference table.
#
#  Output:
#
#    real XD(ND), the abscissas of the updated table,
#    which are all zero.
#
#    real YD(ND), the updated divided difference table.
#
  for j in range ( 0, nd ):

    for i in range ( nd - 2, -1, -1 ):
      yd[i] = yd[i] - xd[i] * yd[i+1]
#
#  Shift the XD values up one position.
#
    xd[1:nd] = xd[0:nd-1]

    xd[0] = 0.0

  return xd, yd

def dif_shift_zero_test ( ):

#*****************************************************************************80
#
## dif_shift_zero_test() tests dif_shift_zero().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  maxtab = 10

  print ( '' )
  print ( 'dif_shift_zero_test():' )
  print ( '  dif_shift_zero() shifts a divided difference' )
  print ( '  table to all zero abscissas' )
  print ( '  These are equivalent operations!' )
#
#  Set XTAB, YTAB to X, F(X)
#
  ntab = 4
  xtab1 = np.arange ( ntab ) + 1.0
  ytab1 = xtab1**3 - 2.0 * xtab1**2 + 3.0 * xtab1 - 4.0

  xtab2 = xtab1.copy()
  ytab2 = ytab1.copy()
#
#  Compute and display the finite difference table.
#
  diftab1 = data_to_dif_display ( ntab, xtab1, ytab1 )

  diftab2 = data_to_dif_display ( ntab, xtab2, ytab2 )
#
#  Examine corresponding polynomial.
#
  dif_print ( ntab, xtab1, diftab1, '  The divided difference polynomial:' )
#
#  Shift to zero.
#
  xtab1, diftab1 = dif_shift_zero ( ntab, xtab1, diftab1 )
  r8poly_print ( diftab1, '  Using dif_shift_zero()' )
#
#  Shift to zero.
#
  c = dif_to_r8poly ( ntab, xtab2, diftab2 )
  r8poly_print ( c, '  Using dif_to_r8poly()' )

  return

def dif_to_r8poly ( ntab, xtab, diftab ):

#*****************************************************************************80
#
## dif_to_r8poly() converts a divided difference table to standard polynomial form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carl deBoor,
#    A Practical Guide to Splines,
#    Springer, 2001,
#    ISBN: 0387953663,
#    LC: QA1.A647.v27.
#
#  Input:
#
#    integer NTAB, the number of coefficients, and abscissas.
#
#    real XTAB(NTAB), the X values used in the divided
#    difference representation of the polynomial.
#
#    real DIFTAB(NTAB), the divided difference table.
#
#  Output:
#
#    real C(NTAB), the standard form polyomial coefficients.
#    C(1) is the constant term, and C(NTAB) is the coefficient
#    of X^(NTAB-1).
#
  c = diftab.copy()
#
#  Recompute the divided difference coefficients.
#
#  I am so sick of these 1/0 shifts!
#  Write these loops the stupid way for now.
#
  for j in range ( 1, ntab ):
    for i in range ( 1, ntab - j + 1 ):
      c[ntab-i-1] = c[ntab-i-1] - xtab[ntab-i-j+1-1] * c[ntab-i+1-1]

  return c

def dif_to_r8poly_test ( ):

#*****************************************************************************80
#
## dif_to_r8poly_test() tests dif_to_r8poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'dif_to_r8poly_test():' )
  print ( '  dif_to_r8poly() converts a divided difference polynomial' )
  print ( '  to the standard power form' )

  nroots = 1
  r = np.array ( [ 3.0 ] )
  r8vec_print ( nroots, r, '  The roots:' )
  ntab, xtab, diftab = roots_to_dif ( nroots, r )
  c = dif_to_r8poly ( ntab, xtab, diftab )
  r8poly_print ( c, '  The polynomial:' )

  nroots = 2
  r = np.array ( [ 3.0, 1.0 ] )
  r8vec_print ( nroots, r, '  The roots:' )
  ntab, xtab, diftab = roots_to_dif ( nroots, r )
  c = dif_to_r8poly ( ntab, xtab, diftab )
  r8poly_print ( c, '  The polynomial:' )

  nroots = 3
  r = np.array ( [ 3.0, 1.0, 2.0 ] )
  r8vec_print ( nroots, r, '  The roots:' )
  ntab, xtab, diftab = roots_to_dif ( nroots, r )
  c = dif_to_r8poly ( ntab, xtab, diftab )
  r8poly_print ( c, '  The polynomial:' )

  nroots = 4
  r = np.array ( [ 3.0, 1.0, 2.0, 4.0 ] )
  r8vec_print ( nroots, r, '  The roots:' )
  ntab, xtab, diftab = roots_to_dif ( nroots, r )
  c = dif_to_r8poly ( ntab, xtab, diftab )
  r8poly_print ( c, '  The polynomial:' )

  return

def dif_value ( nd, xd, yd, xv ):

#*****************************************************************************80
#
## dif_value() evaluates a divided difference polynomial at one or more points.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carl deBoor,
#    A Practical Guide to Splines,
#    Springer, 2001,
#    ISBN: 0387953663,
#    LC: QA1.A647.v27.
#
#  Input:
#
#    integer ND, the order of the difference table.
#
#    real XD(ND), the X values of the difference table.
#
#    real YD(ND), the divided differences.
#
#    real XV(NV), the evaluation points.
#
#  Output:
#
#    real YV(NV), the value of the divided difference
#    polynomial at the evaluation points.
#
  import numpy as np
#
#  If XV is a scalar, we need to make it look like a vector!
#
  xv = np.atleast_1d ( xv )

  nv = xv.shape[0]
  yv = yd[nd-1] * np.ones ( nv )
#
#  Another indexing issue resolved by adding -1 to array indices.
#
  for i in range ( 1, nd ):
    yv[0:nv] = yd[nd-i-1] + ( xv[0:nv] - xd[nd-i-1] ) * yv[0:nv]

  if ( nv == 1 ):
    yv = yv[0]

  return yv

def dif_value_test ( ):

#*****************************************************************************80
#
## dif_value_test() tests dif_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'dif_value_test():' )
  print ( '  dif_value() evaluates a divided difference polynomial.' )
#
#  Set XTAB, YTAB to X, exp(x).
#
  ntab = 4
  xtab = np.arange ( ntab ) + 1.0
  ytab = np.exp ( xtab )

  r8vec2_print ( xtab, ytab, '  The data to be processed:' )

  diftab = data_to_dif ( ntab, xtab, ytab )

  dif_print ( ntab, xtab, diftab, '  The divided difference polynomial:' )
#
#  Evaluate the polynomial between 2 and 3.
#
  n = 11
  x = np.linspace ( 2.0, 3.0, n )
  y = dif_value ( ntab, xtab, diftab, x )
  r8vec2_print ( x, y, '  Polynomial values:' )

  return

def lagrange_rule ( n, x ):

#*****************************************************************************80
#
## lagrange_rule() computes the weights of a Lagrange interpolation rule.
#
#  Discussion:
#
#    Given N abscissas X, an arbitrary function F(X) can be
#    interpolated by a polynomial P(X) of order N (and degree N-1)
#    using weights that depend only on X.
#
#    Standard Lagrange interpolation can be rewritten into this form,
#    which is more economical than evaluating the individual Lagrange
#    basis polynomials.
#
#    If we define
#
#      W(I) = 1 / product ( 1 <= J <= N, J /= I ) ( X(J) - X(I) )
#
#    then
#
#      P(XV) = sum ( 1 <= I <= N ) W(I) * F( X(I) ) / ( XV - X(I) )
#            / sum ( 1 <= I <= N ) W(I)             / ( XV - X(I) )
#
#    except when XV = X(J), for some J, when we set:
#
#      P(X(J)) = F(X(J))
#
#  Modified:
#
#    07 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jean-Paul Berrut, Lloyd Trefethen,
#    Barycentric Lagrange Interpolation,
#    SIAM Review,
#    Volume 46, Number 3, September 2004, pages 501-517.
#
#  Input:
#
#    integer N, the order of the rule.
#
#    real X(N), the abscissas of the rule.
#
#  Output:
#
#    real W(N), the weights of the rule.
#
  import numpy as np

  w = np.ones ( n )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      w[j] = ( x[i] - x[j] ) * w[j]
    w[i] = np.prod ( ( x[0:i] - x[i] ) )

  w = 1.0 / w

  return w

def lagrange_rule_test ( ):

#*****************************************************************************80
#
## lagrange_rule_test() tests lagrange_rule()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'lagrange_rule_test():' )
  print ( '  lagrange_rule() computes weights for a Lagrange rule' )

  n = 8
  x = np.arange ( n, dtype = int ) + 1
  w = lagrange_rule ( n, x )

  r8vec2_print ( x, w, '  (X,W) Lagrange rule weights' )

  return

def lagrange_sum ( n, x, w, y, xv ):

#*****************************************************************************80
#
## lagrange_sum() carries out a Lagrange interpolation rule.
#
#  Discussion:
#
#    It is assumed that LAGRANGE_RULE has already been called to compute
#    the appropriate weights for the given set of abscissas.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jean-Paul Berrut, Lloyd Trefethen,
#    Barycentric Lagrange Interpolation,
#    SIAM Review,
#    Volume 46, Number 3, September 2004, pages 501-517.
#
#  Input:
#
#    integer N, the order of the rule.
#
#    real X(N), the abscissas of the rule.
#
#    real W(N), the weights of the rule.
#
#    real Y(N), the function values at the abscissas.
#
#    real XV, a point where an interpolated value is needed.
#
#  Output:
#
#    real YV, the interpolated function value.
#
  for i in range ( 0, n ):

    if ( xv == x[i] ):
      yv = y[i]
      return yv

  top = 0.0
  bot = 0.0

  for i in range ( 0, n ):
    top = top + w[i] * y[i] / ( xv - x[i] )
    bot = bot + w[i]        / ( xv - x[i] )

  yv = top / bot

  return yv

def lagrange_sum_test ( ):

#*****************************************************************************80
#
## lagrange_sum_test() tests lagrange_sum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'lagrange_sum_test():' )
  print ( '  lagrange_sum() evaluates a Lagrange interpolant' )
#
#  Values of f(x) = x^3 - 12 x^2 + 39 x -28 = ( x - 1 ) * ( x - 4 ) * ( x - 7 )
#
  nd = 4
  xd = np.array ( [ 0.0, 2.0, 5.0, 10.0 ] )
  yd = np.array ( [ -28.0, +10.0, -8.0, +162.0 ] )

  w = lagrange_rule ( nd, xd )

  ni = 11
  xi = np.linspace ( 0.0, 10.0, ni )

  print ( '' )
  print ( '       x      f(x)    Interp' )
  print ( '' )
  for i in range ( 0, ni ):
    yexact = xi[i]**3 - 12 * xi[i]**2 + 39 * xi[i] - 28
    yi = lagrange_sum ( nd, xd, w, yd, xi[i] )
    print ( '  %10.4f  %14.6g  %14.6g' % ( xi[i], yexact, yi ) )

  return

def lagrange_value ( n, x, y, xv ):

#*****************************************************************************80
#
## lagrange_value() applies a naive form of Lagrange interpolation.
#
#  Discussion:
#
#    Given N abscissas X, an arbitrary function Y(X) can be
#    interpolated by a polynomial P(X) of order N (and degree N-1)
#    using Lagrange basis polynomials of degree N-1.
#
#    Standard Lagrange interpolation can be rewritten into this form,
#    which is more economical than evaluating the individual Lagrange
#    basis polynomials.
#
#    If we define
#
#      L(I)(XV) = product ( 1 <= J <= N, J /= I )
#        ( XV - X(J) ) / ( X(I) - X(J) )
#
#    then
#
#      P(XV) = sum ( 1 <= I <= N ) Y( X(I) ) * L(I)(XV)
#
#    Applying this form of the interpolation rule directly involves
#    about N^2 work.  There are more efficient forms of the rule.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data points.
#
#    real X(N), the abscissas.
#
#    real Y(N), the function values at the abscissas.
#
#    real XV, a point where an interpolated value is
#    needed.
#
#  Output:
#
#    real YV, the interpolated function value.
#
  yv = 0.0

  for i in range ( 0, n ):
    poly = 1.0
    for j in range ( 0, n ):
      if ( j != i ):
        poly = poly * ( xv - x[j] ) / ( x[i] - x[j] )

    yv = yv + y[i] * poly

  return yv

def lagrange_value_test ( ):

#*****************************************************************************80
#
## lagrange_value_test() tests lagrange_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nd = 4
  ni = 21
#
#  Values of f(x) = x^3 - 12 x^2 + 39 x -28 = ( x - 1 ) * ( x - 4 ) * ( x - 7 )
#
  xd = np.array ( [ 0.0, 2.0, 5.0, 10.0 ] )
  yd = np.array ( [ -28.0, +10.0, -8.0, +162.0 ] )
 
  print ( '' )
  print ( 'lagrange_value_test():' )
  print ( '  lagrange_value() evaluates a Lagrange 1D interpolant.' )

  x_min = 0.0
  x_max = 10.0
  xi = np.linspace ( x_min, x_max, ni )

  print ( '' )
  print ( '       x      f(x)    Interp' )
  print ( '' )
  for i in range ( 0, ni ):
    yexact = xi[i]**3 - 12 * xi[i]**2 + 39 * xi[i] - 28
    yi = lagrange_value ( nd, xd, yd, xi[i] )
    print ( '  %10.4f  %14.6g  %14.6g' % ( xi[i], yexact, yi ) )

  return

def nc_rule ( norder, a, b, xtab ):

#*****************************************************************************80
#
## nc_rule() computes the weights of a Newton-Cotes quadrature rule.
#
#  Discussion:
#
#    For the interval [A,B], the Newton-Cotes quadrature rule estimates
#
#      Integral ( A <= X <= B ) F(X) dX
#
#    using NORDER equally spaced abscissas XTAB(I) and a weight vector
#    WEIGHT(I):
#
#      Sum ( 1 <= I <= N ) WEIGHT(I) * F ( XTAB(I) ).
#
#    For the CLOSED rule, the abscissas include the points A and B.
#    For the OPEN rule, the abscissas do not include A and B.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NORDER, the order of the rule.
#
#    real A, B, the left and right endpoints of the interval
#    over which the quadrature rule is to be applied.
#
#    real XTAB(NORDER), the abscissas of the rule.
#
#  Output:
#
#    real WEIGHT(NORDER), the weights of the rule.
#
  import numpy as np

  weight = np.zeros ( norder )

  for i in range ( 0, norder ):
#
#  Compute the Lagrange basis polynomial which is 1 at XTAB(I),
#  and zero at the other nodes.
#
    poly_cof = r8poly_basis_1 ( i, norder, xtab )
#
#  Evaluate the antiderivative of the polynomial at the left and
#  right endpoints.
#
    yvala = r8poly_ant_value ( norder-1, poly_cof, a )

    yvalb = r8poly_ant_value ( norder-1, poly_cof, b )

    weight[i] = yvalb - yvala

  return weight

def ncc_rule ( norder ):

#*****************************************************************************80
#
## ncc_rule() computes the coefficients of a Newton-Cotes closed quadrature rule.
#
#  Discussion:
#
#    For the interval [-1,1], the Newton-Cotes quadrature rule estimates
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    using NORDER equally spaced abscissas XTAB(I) and a weight vector
#    WEIGHT(I):
#
#      Sum ( 1 <= I <= N ) WEIGHT(I) * F ( XTAB(I) ).
#
#    For the CLOSED rule, the abscissas include A and B.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NORDER, the order of the rule.
#
#  Output:
#
#    real XTAB(NORDER), the abscissas of the rule.
#
#    real WEIGHT(NORDER), the weights of the rule.
#
  import numpy as np
#
#  Compute a closed quadrature rule.
#
  a = -1.0
  b =  1.0

  xtab = np.zeros ( norder )

  for i in range ( 0, norder ):
    xtab[i] = ( ( norder - i - 1   ) * a   \
              + (          i       ) * b ) \
              / ( norder     - 1 )

  weight = nc_rule ( norder, a, b, xtab )

  return xtab, weight

def ncc_rule_test ( ):

#*****************************************************************************80
#
## ncc_rule_test() tests ncc_rule()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
  norder = 8

  print ( '' )
  print ( 'ncc_rule_test():' )
  print ( '  ncc_rule() computes closed Newton Cotes formulas' )

  xtab, weight = ncc_rule ( norder )

  print ( '' )
  print ( '  Newton-Cotes Closed Quadrature Rule:' )
  print ( '' )
  print ( '      Abscissa       Weight' )
  print ( '' )

  for i in range ( 0, norder ):
    print ( '  %3d  %14f  %14f' % ( i, xtab[i], weight[i] ) )

  return

def nco_rule ( norder ):

#*****************************************************************************80
#
## nco_rule() computes the coefficients of a Newton-Cotes open quadrature rule.
#
#  Discussion:
#
#    For the interval [-1,1], the Newton-Cotes quadrature rule estimates
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    using NORDER equally spaced abscissas XTAB(I) and a weight vector
#    WEIGHT(I):
#
#      Sum ( 1 <= I <= N ) WEIGHT(I) * F ( XTAB(I) ).
#
#    For the OPEN rule, the abscissas do not include A and B.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NORDER, the order of the rule.
#
#  Output:
#
#    real XTAB(NORDER), the abscissas of the rule.
#
#    real WEIGHT(NORDER), the weights of the rule.
#
  import numpy as np

  a = -1.0
  b =  1.0

  xtab = np.zeros ( norder )

  for i in range ( 0, norder ):
    xtab[i] = ( ( norder - i     ) * a   \
              + (          i + 1 ) * b ) \
              / ( norder     + 1 )

  weight = nc_rule ( norder, a, b, xtab )

  return xtab, weight

def nco_rule_test ( ):

#*****************************************************************************80
#
## nco_rule_test() tests nco_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
  norder = 8

  print ( '' )
  print ( 'nco_rule_test():' )
  print ( '  nco_rule() computes open Newton Cotes formulas.' )

  xtab, weight = nco_rule ( norder )

  print ( '' )
  print ( '  Newton-Cotes Open Quadrature Rule:' )
  print ( '' )
  print ( '      Abscissa       Weight' )
  print ( '' )

  for i in range ( 0, norder ):
    print ( '  %3d  %14f  %14f' % ( i, xtab[i], weight[i] ) )

  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print() prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_test ( ):

#*****************************************************************************80
#
## r8mat_print_test() tests r8mat_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_print_test():' )
  print ( '  r8mat_print() prints an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = float )
  r8mat_print ( m, n, v, '  Here is an R8MAT:' )

  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some() prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_print_some_test ( ):

#*****************************************************************************80
#
## r8mat_print_some_test() tests r8mat_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_print_some_test():' )
  print ( '  r8mat_print_some() prints some of an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = float )
  r8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:' )

  return

def r8mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_transpose_print() prints an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_transpose_print_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_print_test() tests r8mat_transpose_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_transpose_print_test():' )
  print ( '  r8mat_transpose_print() prints an R8MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = float )
  r8mat_transpose_print ( m, n, v, '  Here is an R8MAT, transposed:' )

  return

def r8mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_transpose_print_some() prints a portion of an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for i2lo in range ( max ( ilo, 0 ), min ( ihi, m - 1 ), incx ):

    i2hi = i2lo + incx - 1
    i2hi = min ( i2hi, m - 1 )
    i2hi = min ( i2hi, ihi )
    
    print ( '' )
    print ( '  Row: ', end = '' )

    for i in range ( i2lo, i2hi + 1 ):
      print ( '%7d       ' % ( i ), end = '' )

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( '%7d :' % ( j ), end = '' )
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_print_some_test() tests r8mat_transpose_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_transpose_print_some_test():' )
  print ( '  r8mat_transpose_print_some() prints some of an R8MAT, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = float )
  r8mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:' )

  return

def r8poly_ant_coef ( n, poly_cof ):

#*****************************************************************************80
#
## r8poly_ant_coef() integrates a polynomial in standard form.
#
#  Discussion:
#
#    The antiderivative of a polynomial P(X) is any polynomial Q(X)
#    with the property that d/dX Q(X) = P(X).
#
#    This routine chooses the antiderivative whose constant term is zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 October 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#    real POLY_COF(1:N+1), the polynomial coefficients.
#    POLY_COF(1) is the constant term, and POLY_COF(N+1) is the
#    coefficient of X^(N).
#
#  Output:
#
#    real POLY_COF2(1:N+2), the coefficients of
#    the antiderivative polynomial, in standard form.  The constant
#    term is set to zero.
#
  import numpy as np

  poly_cof2 = np.zeros ( n + 2 )
#
#  Set the constant term.
#
  poly_cof2[0] = 0.0
#
#  Integrate the polynomial.
#
  for i in range ( 1, n + 2 ):
    poly_cof2[i] = poly_cof[i-1] / float ( i )

  return poly_cof2

def r8poly_ant_coef_test ( ):

#*****************************************************************************80
#
## r8poly_ant_coef_test() tests r8poly_ant_coef().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 October 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  print ( '' )
  print ( 'r8poly_ant_coef_test():' )
  print ( '  r8poly_ant_coef() computes the coefficients of the' )
  print ( '  antiderivative of a polynomial' )

  poly_cof = np.zeros ( n + 1 )
  for i in range ( 0, n + 1 ):
    poly_cof[i] = float ( i + 1 )

  r8poly_print ( poly_cof, '  Polynomial p(x):' )

  poly_cof2 = r8poly_ant_coef ( n, poly_cof )

  r8poly_print ( poly_cof2, '  Antideriv(p(x)):' )

  return

def r8poly_ant_value ( n, poly_cof, xval ):

#*****************************************************************************80
#
## r8poly_ant_value() evaluates evaluates the antiderivative of a polynomial.
#
#  Discussion:
#
#    The constant term of the antiderivative is taken to be zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n, the order of the polynomial.
#
#    real poly_cof(0:n), the polynomial coefficients.  
#    poly_cof(I) is the coefficient of X^I.
#
#    real xval, the evaluation point.
#
#  Output:
#
#    real yval, the polynomial value.
#
  yval = 0.0
  for i in range ( n, -1, -1 ):
    yval = ( yval + poly_cof[i] / float ( i + 1 ) ) * xval

  return yval

def r8poly_ant_value_test ( ):

#*****************************************************************************80
#
## r8poly_ant_value_test() tests r8poly_ant_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4;
  n = 16;
  c = np.array ( [ 24.0, -50.0, +35.0, -10.0, 1.0 ] )

  print ( '' )
  print ( 'r8poly_ant_value_test():' )
  print ( '  r8poly_ant_value() evaluates the antiderivative of a polynomial at a point' )
  print ( '  using a naive method.' )

  r8poly_print ( c, '  The polynomial coefficients:' )

  x_lo = 0.0
  x_hi = 5.0
  x = np.linspace ( x_lo, x_hi, n )

  print ( '' )
  print ( '   I    X    antiP(X)' )
  print ( '' )

  for i in range ( 0, n ):
    p = r8poly_ant_value ( m, c, x[i] )
    print ( '  %2d  %8.4f  %14.6g' % ( i, x[i], p ) )

  return

def r8poly_basis ( ntab, xtab ):

#*****************************************************************************80
#
## r8poly_basis() computes all Lagrange basis polynomial in standard form.
#
#  Discussion:
#
#    The I-th Lagrange basis polynomial for a set of NTAB X values XTAB,
#    L(I,NTAB,XTAB)(X) is a polynomial of order NTAB-1 which is zero at
#    XTAB(J) for J not equal to I, and 1 when J is equal to I.
#
#    The Lagrange basis polynomials have the property that the interpolating
#    polynomial through a set of NTAB data points (XTAB,YTAB) may be
#    represented as
#
#      P(X) = Sum ( 1 <= I <= N ) YTAB(I) * L(I,NTAB,XTAB)(X)
#
#    Higher order interpolation at selected points may be accomplished
#    using repeated X values, and scaled derivative values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NTAB, the number of data points XTAB.
#
#    real XTAB(NTAB), the X values upon which the
#    Lagrange basis polynomial is to be based.
#
#  Output:
#
#    real POLY_COF(NTAB,NTAB), the polynomial
#    coefficients for the I-th Lagrange basis polynomial are stored
#    in column I.  POLY_COF(1,I) is the constant term, and POLY_COF(1,NTAB)
#    is the coefficient of X**(NTAB-1).
#
  import numpy as np
#
#  Initialize POLY_COF to the identity matrix.
#
  poly_cof = np.zeros ( [ ntab, ntab ] )

  for i in range ( 0, ntab ):
    poly_cof[i,i] = 1.0
#
#  Compute the divided difference table for the IVAL-th Lagrange basis
#  polynomial.
#
  for i in range ( 0, ntab ):
    poly_cof[:,i] = data_to_dif ( ntab, xtab, poly_cof[:,i] ) 
#
#  Convert divided difference coefficients to standard polynomial coefficients.
#
  for i in range ( 0, ntab ):
    poly_cof[:,i] = dif_to_r8poly ( ntab, xtab, poly_cof[:,i] )

  return poly_cof

def r8poly_basis_test ( ):

#*****************************************************************************80
#
## r8poly_basis_test() tests r8poly_basis().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  ntab = 5
  nstep = 9

  print ( '' )
  print ( 'r8poly_basis_test():' )
  print ( '  r8poly_basis() computes Lagrange basis polynomials' )
  print ( '  in standard form.' )
  print ( '' )
#
#  Set the base points.
#
  xtab = np.arange ( ntab ) + 1.0
#
#  Get the difference tables for the basis polynomials and print them.
#
  polcof = r8poly_basis ( ntab, xtab )

  for i in range ( 0, ntab ):
    print ( '  ', end = '' )
    for j in range ( 0, ntab ):
      print ( '%14f' % ( polcof[i,j] ), end = '' )
    print ( '' )
#
#  Print basis polynomial 3 in polynomial form.
#
  d = ntab - 1
  r8poly_print ( polcof[:,2], '  Basis polynomial 2 in standard form:' )
#
#  Evaluate basis polynoimial 3 at a set of points.
#
  print ( '' )
  print ( '  Evaluate basis polynomial 2 at a set of points.' )
  print ( '' )
  print ( '      X        Y' )
  print ( '' )
  xhi =  ntab
  xlo = 1.0

  for i in range ( 0, nstep ):

    xval = ( ( nstep - i - 1 ) * xlo   \
           + (         i     ) * xhi ) \
           / ( nstep     - 1 )

    yval = r8poly_value_horner ( ntab-1, polcof[:,2], xval )

    print ( '  %14f  %14f' % ( xval, yval ) )

  return

def r8poly_basis_1 ( ival, ntab, xtab ):

#*****************************************************************************80
#
## r8poly_basis_1() computes the I-th Lagrange basis polynomial in standard form.
#
#  Discussion:
#
#    The I-th Lagrange basis polynomial for a set of NTAB X values XTAB,
#    L(I,NTAB,XTAB)(X) is a polynomial of order NTAB-1 which is zero at
#    XTAB(J) for J not equal to I, and 1 when J is equal to I.
#
#    The Lagrange basis polynomials have the property that the interpolating
#    polynomial through a set of NTAB data points (XTAB,YTAB) may be
#    represented as
#
#      P(X) = Sum ( 1 <= I <= N ) YTAB(I) * L(I,NTAB,XTAB)(X)
#
#    Higher order interpolation at selected points may be accomplished
#    using repeated X values, and scaled derivative values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer IVAL, the index of the desired Lagrange basis polynomial.
#    IVAL should be between 0 and NTAB-1.
#
#    integer NTAB, the number of data points XTAB.
#
#    real XTAB(NTAB), the X values upon which the
#    Lagrange basis polynomial is to be based.
#
#  Output:
#
#    real POLY_COF(1:NTAB), the polynomial coefficients for the IVAL-th 
#    Lagrange basis polynomial.
#
  import numpy as np
#
#  Check IVAL.
#
  if ( ival < 0 or ntab - 1 < ival ):
    print ( '' )
    print ( 'r8poly_base_1(): Fatal error!' )
    print ( '  IVAL must be between 1 and ', ntab )
    print ( '  but your value is ', ival )
    raise Exception ( 'r8poly_base_1(): Fatal error!' )
#
#  Initialize POLY_COF to the IVAL-th column of the identity matrix.
#
  poly_cof = np.zeros ( ntab )
  poly_cof[ival] = 1.0
#
#  Compute the divided difference table for the IVAL-th Lagrange basis
#  polynomial.
#
  poly_cof = data_to_dif ( ntab, xtab, poly_cof )
#
#  Convert the divided difference table coefficients to standard polynomial
#  coefficients.
#
  poly_cof = dif_to_r8poly ( ntab, xtab, poly_cof )

  return poly_cof

def r8poly_deriv_coef ( n, c, p ):

#*****************************************************************************80
#
## r8poly_deriv_coef() returns the derivative of a polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the degree of the polynomial.
#
#    real C(1:N+1), the polynomial coefficients.
#    C(I+1) is the coefficient of X**I.
#
#    integer P, the order of the derivative.
#    0 means no derivative is taken.
#    1 means first derivative,
#    2 means second derivative and so on.
#    Values of P less than 0 are meaningless.  Values of P greater
#    than N are meaningful, but the code will behave as though the
#    value of P was N.
#
#  Output:
#
#    real CP(1:N+1-P), the polynomial coefficients of
#    the derivative.
#
  import numpy as np

  if ( n <= p ):
    cp = np.zeros ( 1 )
    return cp

  cp_temp = c.copy ( )

  for d in range ( 1, p + 1 ):
    for i in range ( 0, n + 1 - d ):
      cp_temp[i] = float ( i + 1 ) * cp_temp[i+1]
    cp_temp[n-d+1] = 0.0

  cp = cp_temp[0:n+1-p].copy ( )

  return cp

def r8poly_deriv_coef_test ( ):

#*****************************************************************************80
#
## r8poly_deriv_coef_test() tests r8poly_deriv_coef().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
  n = 4

  print ( '' )
  print ( 'r8poly_deriv_coef_test():' )
  print ( '  r8poly_deriv() computes the coefficients of' )
  print ( '  the derivative of a polynomial.' )

  x = r8vec_indicator1 ( n )

  c = roots_to_r8poly ( n, x )

  r8poly_print ( c, '  The initial polynomial' )

  for d in range ( 0, n + 1 ):
    cp = r8poly_deriv_coef ( n, c, d )
    label = '  The derivative of order %d' % ( d )
    r8poly_print ( cp, label )

  return

def r8poly_deriv_value ( d, c, xval ):

#*****************************************************************************80
#
## r8poly_deriv_value() evaluates the derivative of a polynomial in standard form.
#
#  Discussion:
#
#    A polynomial in standard form, with coefficients POLY_COF(*),
#    may be written:
#
#      P(X) = C(1)
#           + C(2) * X
#           ...
#           + C(D+1) * X^(D)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer D, the degree of the polynomial.
#
#    real C(1:D+1), the polynomial coefficients.
#    C(1) is the constant term, and C(N) is the coefficient of X^(N-1).
#
#    real XVAL, a value where the derivative of the
#    polynomial is to be evaluated.
#
#  Output:
#
#    real YVAL, the value of the derivative of the
#    polynomial at XVAL.
#
  yval = d * c[d]

  for i in range ( d - 1, 0, -1 ):
    yval = yval * xval + i * c[i]

  return yval

def r8poly_deriv_value_test ( ):

#*****************************************************************************80
#
## r8poly_deriv_value_test() tests r8poly_deriv_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8poly_deriv_value_test():' )
  print ( '  r8poly_deriv_value() evaluates the derivative of a polynomial.' )

  d = 4
  x = np.arange ( d ) + 1.0
  c = roots_to_r8poly ( d, x )
  r8poly_print ( c, '  The polynomial' )

  print ( '' )
  print ( '  A table of derivative values:' )
  print ( '' )
  x = np.linspace ( 0.0, 4.0, 9 )
  for i in range ( 0, 9 ):
    y = r8poly_deriv_value ( d, c, x[i] )
    print ( '  %8.4f  %8.4f' % ( x[i], y ) )

  return

def r8poly_order ( m, a ):

#*****************************************************************************80
#
## r8poly_order() returns the order of a polynomial.
#
#  Discussion:
#
#    The order of a constant polynomial is 1.
#    The order of the zedro polynomial is debatable, but this routine
#    returns it as 0.
#
#    The order of a polynomial is the index of the highest power
#    of X with a nonzero coefficient.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the nominal degree of A.
#
#    real A[0:M], the coefficients of the polynomials.
#
#  Output:
#
#    integer VALUE, the degree of A.
#
  value = m

  while ( 0 < value ):
    if ( a[value] != 0.0 ):
      break
    value = value - 1

  return value

def r8poly_order_test ( ):

#*****************************************************************************80
#
## r8poly_order_test() tests r8poly_order().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  c1 = np.array ( [ 1.0, 2.0, 3.0, 4.0 ] )
  c2 = np.array ( [ 1.0, 2.0, 3.0, 0.0 ] )
  c3 = np.array ( [ 1.0, 2.0, 0.0, 4.0 ] )
  c4 = np.array ( [ 1.0, 0.0, 0.0, 0.0 ] )
  c5 = np.array ( [ 0.0, 0.0, 0.0, 0.0 ] )

  print ( '' )
  print ( 'r8poly_order_test():' )
  print ( '  r8poly_order() determines the order of an R8POLY.' )

  m = 3

  r8poly_print ( c1, '  The R8POLY:' )
  d = r8poly_order ( m, c1 )
  print ( '  Dimension = %d,  Actual order = %d' % ( m, d ) )

  r8poly_print ( c2, '  The R8POLY:' )
  d = r8poly_order ( m, c2 )
  print ( '  Dimension = %d,  Actual order = %d' % ( m, d ) )

  r8poly_print ( c3, '  The R8POLY:' )
  d = r8poly_order ( m, c3 )
  print ( '  Dimension = %d,  Actual order = %d' % ( m, d ) )

  r8poly_print ( c4, '  The R8POLY:' )
  d = r8poly_order ( m, c4 )
  print ( '  Dimension = %d,  Actual order = %d' % ( m, d ) )

  r8poly_print ( c5, '  The R8POLY:' )
  d = r8poly_order ( m, c5 )
  print ( '  Dimension = %d,  Actual order = %d' % ( m, d ) )

  return

def r8poly_print ( a, title ):

#*****************************************************************************80
#
## r8poly_print() prints a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A[M+1], the polynomial coefficients.
#    A[0] is the constant term and
#    A[M] is the coefficient of X^M.
#
#    string TITLE, a title.
#
  import numpy as np

  m = len ( a ) - 1

  print ( title )

  if ( np.all ( a == 0.0 ) ):
    print ( '  p(x) = 0' )
    return
 
  first = True

  for i in range ( m, -1, -1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0.0 ):

      if ( first ):
        print ( '  p(x) =', end = '' )
        if ( plus_minus == '+' ):
          plus_minus = ' '
        first = False

      if ( 2 <= i ):
        print ( ' %c %g * x^%d' % ( plus_minus, mag, i ), end = '' )
      elif ( i == 1 ):
        print ( ' %c %g * x' % ( plus_minus, mag ), end = '' )
      elif ( i == 0 ):
        print ( ' %c %g' % ( plus_minus, mag ), end = '' )

  print ( '' )

  return

def r8poly_print_test ( ):

#*****************************************************************************80
#
## r8poly_print_test() tests r8poly_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8poly_print_test():' )
  print ( '  r8poly_print() prints an R8POLY.' )

  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 9.0 ] )
  print ( '' )
  r8poly_print ( c, '  The R8POLY:' )

  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 0.0 ] )
  print ( '' )
  r8poly_print ( c, '  The R8POLY:' )

  c = np.array ( [ 12.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )
  print ( '' )
  r8poly_print ( c, '  The R8POLY:' )

  c = np.array ( [ 0.0, 0.0, 0.0, 0.0, 0.0, 1.0 ] )
  print ( '' )
  r8poly_print ( c, '  The R8POLY:' )

  c = np.array ( [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )
  print ( '' )
  r8poly_print ( c, '  The R8POLY:' )

  return

def r8poly_shift ( n, poly_cof, scale, shift ):

#*****************************************************************************80
#
## r8poly_shift() adjusts the coefficients of a polynomial for a new argument.
#
#  Discussion:
#
#    Assuming P(X) is a polynomial in the argument X, of the form:
#
#      P(X) =
#          C(N) * X^(N-1)
#        + ...
#        + C(2) * X
#        + C(1),
#
#    and that Z is related to X by the formula:
#
#      Z = SCALE * X + SHIFT
#
#    then this routine computes coefficients C for the polynomial Q(Z):
#
#      Q(Z) =
#          C(N) * Z^(N-1)
#        + ...
#        + C(2) * Z
#        + C(1)
#
#    so that:
#
#      Q(Z(X)) = P(X)e
#
#  Example:
#
#    P(X) = 2 * X^2 - X + 6
#
#    Z = 2.0 * X + 3.0
#
#    Q(Z) = 0.5 *         Z^2 -  3.5 * Z + 12
#
#    Q(Z(X)) = 0.5 * ( 4.0 * X^2 + 12.0 * X +  9 )
#            - 3.5 * (              2.0 * X +  3 )
#                                            + 12
#
#            = 2.0         * X^2 -  1.0 * X +  6
#
#            = P(X)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#    real POLY_COF(N), the coefficient array in terms of the X variable.
#
#    real SHIFT, SCALE, the shift and scale applied to X,
#    so that Z = SCALE * X + SHIFT.
#
#  Output:
#
#    real POLY_COF(N), the coefficient array in terms of the Z variable.
#
  for i in range ( 0, n ):
    poly_cof[(i+1):n] = poly_cof[(i+1):n] / scale

  for i in range ( 0, n ):
    for j in range ( n - 2, i - 1, -1 ):
      poly_cof[j] = poly_cof[j] - shift * poly_cof[j+1]

  return poly_cof

def r8poly_shift_test ( ):

#*****************************************************************************80
#
## r8poly_shift_test() tests r8poly_shift().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8poly_shift_test():' )
  print ( '  r8poly_shift() shifts an R8POLY p(x) to q(z)' )
  print ( '  where z=scale*x+shift.' )

  order = 3
  c = np.array ( [ 6.0, -1.0, 2.0 ] )
  r8poly_print ( c, '  p(x):' )

  scale = 2.0
  shift = 3.0
  print ( '' )
  print ( '  z = scale * x + shift' )
  print ( '  Scale = ', scale )
  print ( '  Shift = ', shift )

  c2 = r8poly_shift ( order, c, scale, shift )
  r8poly_print ( c2, '  q(z):' )

  c3 = np.array ( [ 12.0, -3.5, 0.5 ] )
  r8poly_print ( c3, '  Expected q(z):' )

  return

def r8poly_value_horner ( m, c, x ):

#*****************************************************************************80
#
## r8poly_value_horner() evaluates a polynomial using Horner's method.
#
#  Discussion:
#
#    The polynomial 
#
#      p(x) = c0 + c1 * x + c2 * x^2 + ... + cm * x^m
#
#    is to be evaluated at the value X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the degree.
#
#    real C(0:M), the polynomial coefficients.  
#    C(I) is the coefficient of X^I.
#
#    real X, the evaluation point.
#
#  Output:
#
#    real VALUE, the polynomial value.
#
  value = c[m]
  for i in range ( m - 1, -1, -1 ):
    value = value * x + c[i]

  return value

def r8poly_value_horner_test ( ):

#*****************************************************************************80
#
## r8poly_value_horner_test() tests r8poly_value_horner().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4;
  n = 16;
  c = np.array ( [ 24.0, -50.0, +35.0, -10.0, 1.0 ] )

  print ( '' )
  print ( 'r8poly_value_horner_test():' )
  print ( '  r8poly_value_horner() evaluates a polynomial at a point' )
  print ( '  using Horners method.' )

  r8poly_print ( c, '  The polynomial coefficients:' )

  x_lo = 0.0
  x_hi = 5.0
  x = np.linspace ( x_lo, x_hi, n )

  print ( '' )
  print ( '   I    X    P(X)' )
  print ( '' )

  for i in range ( 0, n ):
    p = r8poly_value_horner ( m, c, x[i] )
    print ( '  %2d  %8.4f  %14.6g' % ( i, x[i], p ) )

  return

def r8vec_indicator1 ( n ):

#*****************************************************************************80
#
## r8vec_indicator1() sets an R8VEC to the indicator vector (1,2,3,...).
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of the vector.
#
#  Output:
#
#    real A(N), the indicator array.
#
  import numpy as np

  a = np.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_indicator1_test ( ):

#*****************************************************************************80
#
## r8vec_indicator1_test() tests r8vec_indicator1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_indicator1_test():' )
  print ( '  r8vec_indicator1() returns the 1-based indicator matrix.' )

  n = 10
  a = r8vec_indicator1 ( n )

  r8vec_print ( n, a, '  The 1-based indicator vector:' )

  return

def r8vec_is_distinct ( n, a ):

#*****************************************************************************80
#
## r8vec_is_distinct() is true if the entries in an R8VEC are distinct.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector to be checked.
#
#  Output:
#
#    bool VALUE is true if the elements of A are distinct.
#
  for i in range ( 1, n ):
    for j in range ( 0, i ):
      if ( a[i] == a[j] ):
        value = False;
        return value

  value = True

  return value

def r8vec_is_distinct_test ( ):

#*****************************************************************************80
#
## r8vec_is_distinct_test() tests r8vec_is_distinct().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_is_distinct_test():' )
  print ( '  r8vec_is_distinct() computes the maximum entry in an R8VEC.' )

  n = 5
  a = np.array ( [ 1.0, 2.0, 5.0, 3.0, 4.0 ] )
  r8vec_print ( n, a, '  Input vector:' )
  if ( r8vec_is_distinct ( n, a ) ):
    print ( '  Array entries are distinct.' )
  else:
    print ( '  Array entries are NOT distinct.' )

  n = 5
  a = np.array ( [ 1.0, 2.0, 5.0, 2.0, 4.0 ] )
  r8vec_print ( n, a, '  Input vector:' )
  if ( r8vec_is_distinct ( n, a ) ):
    print ( '  Array entries are distinct.' )
  else:
    print ( '  Array entries are NOT distinct.' )

  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

  return

def r8vec_print_test ( ):

#*****************************************************************************80
#
## r8vec_print_test() tests r8vec_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_print_test():' )
  print ( '  r8vec_print() prints an R8VEC.' )
#
#  Use r8vec_print:
#
  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = float )
  label = '  Use r8vec_print():'
  r8vec_print ( n, v, label )
#
#  Use Python print() for data.
#
  print ( '' )
  print ( '  Use python print():' )
  print ( '' )
  print ( v )

  return

def r8vec_transpose_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_transpose_print() prints an R8VEC "transposed".
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Example:
#
#    A = (/ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 /)
#    TITLE = 'My vector:  '
#
#    My vector:   1.0    2.1    3.2    4.3    5.4
#                 6.5    7.6    8.7    9.8   10.9
#                11.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  title_length = len ( title )

  for ilo in range ( 0, n, 5 ):

    if ( ilo == 0 ):
      print ( title, end = '' )
    else:
      blanks = ''
      for i in range ( 0, title_length ):
        blanks = blanks + ' '
      print ( blanks, end = '' )

    print ( '  ', end = '' )

    ihi = min ( ilo + 5 - 1, n - 1 )

    for i in range ( ilo, ihi + 1 ):
      print ( '  %12g' % ( a[i] ), end = '' )
    print ( '' )

  return

def r8vec_transpose_print_test ( ):

#*****************************************************************************80
#
## r8vec_transpose_print_test() tests r8vec_transpose_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 11

  print ( '' )
  print ( 'r8vec_transpose_print_test():' )
  print ( '  r8vec_transpose_print() prints an R8VEC "tranposed",' )
  print ( '  that is, placing multiple entries on a line.' )

  x = np.array ( [ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 ] )

  r8vec_transpose_print ( n, x, '  The vector X:' )

  return

def r8vec2_print ( a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  n = len ( a1 )

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## r8vec2_print_test() tests r8vec2_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec2_print_test():' )
  print ( '  r8vec2_print() prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( v, w, '  Print a pair of R8VEC\'s:' )

  return

def roots_to_dif ( nroots, r ):

#*****************************************************************************80
#
## roots_to_dif() sets a divided difference table for a polynomial from its roots.
#
#  Discussion:
#
#    This turns out to be a simple task, because of two facts:
#
#    * The divided difference polynomial of one smaller degree which
#      passes through the values ( ROOT(I), 0 ) is the zero polynomial,
#      and hence has a zero divided difference table.
#
#    * We want a polynomial of one degree higher, but we don't want it
#      to pass through an addditional point.  Instead, we specify that
#      the polynomial is MONIC.  This means that the divided difference
#      table is almost the same as for the zero polynomial, except that
#      there is one more pair of entries, an arbitrary X value, and
#      a Y value of 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NROOTS, is the number of roots.
#
#    real R(NROOTS), the roots of the polynomial.
#
#  Output:
#
#    integer NTAB, is equal to NROOTS+1.
#
#    real XTAB(NTAB), the abscissas of the divided
#    difference table.
#
#    real DIFTAB(NTAB), the divided difference table.
#
  import numpy as np

  ntab = nroots + 1
#
#  Build the appropriate difference table for the polynomial
#  through ( R(I), 0 ) of degree NTAB-2.
#
  diftab = np.zeros ( ntab )
#
#  Append the extra data to make a monic polynomial of degree NTAB-1
#  which is zero at the NTAB-1 roots.
# 
  xtab = np.zeros ( ntab )
  xtab[0:ntab-1] = r.copy ( )

  diftab[ntab-1] = 1.0

  return ntab, xtab, diftab

def roots_to_dif_test ( ):

#*****************************************************************************80
#
## roots_to_dif_test() tests roots_to_dif().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'roots_to_dif_test():' )
  print ( '  roots_to_dif() computes the divided difference polynomial' )
  print ( '  from the set of roots.' )
  print ( '' )

  nroots = 1
  r = np.array ( [ 3.0 ] )
  r8vec_print ( nroots, r, '  The roots:' )
  nc, xtab, diftab = roots_to_dif ( nroots, r )
  dif_print ( nc, xtab, diftab, '  The polynomial:' )

  nroots = 2
  r = np.array ( [ 3.0, 1.0 ] )
  r8vec_print ( nroots, r, '  The roots:' )
  nc, xtab, diftab = roots_to_dif ( nroots, r )
  dif_print ( nc, xtab, diftab, '  The polynomial:' )

  nroots = 3
  r = np.array ( [ 3.0, 1.0, 2.0 ] )
  r8vec_print ( nroots, r, '  The roots:' )
  nc, xtab, diftab = roots_to_dif ( nroots, r )
  dif_print ( nc, xtab, diftab, '  The polynomial:' )

  nroots = 4
  r = np.array ( [ 3.0, 1.0, 2.0, 4.0 ] )
  r8vec_print ( nroots, r, '  The roots:' )
  nc, xtab, diftab = roots_to_dif ( nroots, r )
  dif_print ( nc, xtab, diftab, '  The polynomial:' )

  return

def roots_to_r8poly ( n, x ):

#*****************************************************************************80
#
## roots_to_r8poly() converts polynomial roots to polynomial coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2005
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of roots specified.
#
#    real X(N), the roots.
#
#  Output:
#
#    real C(1:N+1), the coefficients of the polynomial.
#
  import numpy as np
#
#  Initialize C to (0, 0, ..., 0, 1).
#  Essentially, we are setting up a divided difference table.
#
  c = np.zeros ( n + 1 )
  c[n] = 1.0
#
#  Convert to standard polynomial form by shifting the abscissas
#  of the divided difference table to 0.
#
  for j in range ( 1, n + 1 ):
    for i in range ( 1, n + 2 - j ):
      c[n-i] = c[n-i] - x[n+1-i-j] * c[n-i+1]

  return c

def roots_to_r8poly_test ( ):

#*****************************************************************************80
#
## roots_to_r8poly_test() tests roots_to_r8poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  x = np.array ( [ \
     1.0, \
    -4.0, \
     3.0, \
     0.0, \
     3.0 ] );

  print ( '' )
  print ( 'roots_to_r8poly_test():' )
  print ( '  roots_to_r8poly() is given N real roots,' )
  print ( '  and constructs the coefficient vector' )
  print ( '  of the corresponding polynomial.' )

  r8vec_print ( n, x, '  N real roots:' )

  c = roots_to_r8poly ( n, x )

  r8poly_print ( c, '  The polynomial:' )

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
  divdif_test ( )
  timestamp ( )

