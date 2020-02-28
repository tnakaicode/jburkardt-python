#! /usr/bin/env python3
#
def r8poly2_val2 ( dim_num, ndata, tdata, ydata, left, tval ):

#*****************************************************************************80
#
## R8POLY2_VAL2 evaluates a parabolic interpolant through tabular data.
#
#  Discussion:
#
#    This routine is a utility routine used by OVERHAUSER_SPLINE_VAL.
#    It constructs the parabolic interpolant through the data in
#    3 consecutive entries of a table and evaluates this interpolant
#    at a given abscissa value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 September 2006
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIM_NUM, the dimension of a single data point.
#    DIM_NUM must be at least 1.
#
#    Input, integer NDATA, the number of data points.
#    NDATA must be at least 3.
#
#    Input, real TDATA(NDATA), the abscissas of the data points.
#    The values in TDATA must be in strictly ascending order.
#
#    Input, real YDATA(DIM_NUM,NDATA), the data points 
#    corresponding to the abscissas.
#
#    Input, integer LEFT, the location of the first of the three
#    consecutive data points through which the parabolic interpolant
#    must pass.  1 <= LEFT <= NDATA - 2.
#
#    Input, real TVAL, the value of T at which the parabolic
#    interpolant is to be evaluated.  Normally, TDATA(1) <= TVAL <= T(NDATA),
#    and the data will be interpolated.  For TVAL outside this range,
#    extrapolation will be used.
#
#    Output, real YVAL(DIM_NUM), the value of the parabolic
#    interpolant at TVAL.
#
  import numpy as np
  from sys import exit
#
#  Check.
#
  if ( left < 1 or ndata - 2 < left ):
    print ( '' )
    print ( 'R8POLY2_VAL2 - Fatal error!' )
    print ( '  LEFT < 1 or NDATA-2 < LEFT.' )
    print ( '  LEFT = #d', left )
    exit ( 'R8POLY2_VAL2 - Fatal error!' )

  if ( dim_num < 1 ):
    print ( '' )
    print ( 'R8POLY2_VAL2 - Fatal error!' )
    print ( '  DIM_NUM < 1.' )
    print ( '  DIM_NUM = %d' % ( dim_num ) )
    exit ( 'R8POLY2_VAL2 - Fatal error!' )
#
#  Copy out the three abscissas.
#
  t1 = tdata[left-1]
  t2 = tdata[left]
  t3 = tdata[left+1]

  if ( t2 <= t1 or t3 <= t2 ):
    print ( '' )
    print ( 'R8POLY2_VAL2 - Fatal error!' )
    print ( '  T2 <= T1 or T3 <= T2.' )
    print ( '  T1 = #f', t1 )
    print ( '  T2 = #f', t2 )
    print ( '  T3 = #f', t3 )
    exit ( 'R8POLY2_VAL2 - Fatal error!' )
#
#  Construct and evaluate a parabolic interpolant for the data
#  in each dimension.
#
  yval = np.zeros ( dim_num )

  for i in range ( 0, dim_num ):

    y1 = ydata[i,left-1]
    y2 = ydata[i,left]
    y3 = ydata[i,left+1]

    dif1 = ( y2 - y1 ) / ( t2 - t1 )
    dif2 = ( ( y3 - y1 ) / ( t3 - t1 ) \
           - ( y2 - y1 ) / ( t2 - t1 ) ) / ( t3 - t2 )

    yval[i] = y1 + ( tval - t1 ) * ( dif1 + ( tval - t2 ) * dif2 )

  return yval

def r8poly2_val2_test ( ):

#*****************************************************************************80
#
## R8POLY2_VAL2_TEST tests R8POLY2_VAL2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  ndata = 5
  dim_num = 2

  print ( '' )
  print ( 'R8POLY2_VAL2_TEST' )
  print ( '  R8POLY2_VAL2 evaluates parabolas through' )
  print ( '  3 points in a table' )
  print ( '' )
  print ( '  Our data tables will actually be parabolas:' )
  print ( '    A: 2*x^2 + 3 * x + 1.' )
  print ( '    B: 4*x^2 - 2 * x + 5.' )
  print ( '' )

  xdata = np.zeros ( ndata )
  ydata = np.zeros ( [ 2, ndata ] )

  for i in range ( 0, ndata ):
    xval = 2.0 * i
    xdata[i] = xval
    ydata[0,i] = 2.0 * xval * xval + 3.0 * xval + 1.0
    ydata[1,i] = 4.0 * xval * xval - 2.0 * xval + 5.0
    print ( '  %6d  %12f  %12f  %12f' % \
      ( i, xdata[i], ydata[0,i], ydata[1,i] ) )

  print ( '' )
  print ( '  Interpolated data:' )
  print ( '' )
  print ( '  LEFT, X, Y1, Y2' )
  print ( '' )

  for i in range ( 0, 5 ):
    xval = 2 * i + 1
    left = max ( min ( i + 1, ndata - 2 ), 1 )
    yval = r8poly2_val2 ( dim_num, ndata, xdata, ydata, left, xval )
    print ( '  %8d  %12f  %12f  %12f' % ( left, xval, yval[0], yval[1] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY2_VAL2_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly2_val2_test ( )
  timestamp ( )


