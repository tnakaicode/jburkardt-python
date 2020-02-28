#! /usr/bin/env python
#
def r8vec_rsquared ( n, y_data, y_model ):

#*****************************************************************************80
#
## R8VEC_RSQUARED computes the R^2 goodness of fit measurement.
#
#  Discussion:
#
#    We suppose a set of N data values Y_DATA are known, and that a
#    formula or model has generated a corresponding set of Y_MODEL values.
#
#    R^2 measures the extent to which the variation in Y_DATA is captured
#    by the model data Y_MODEL.  If the model is linear, then a value
#    of R^2=1 is optimal, and R^2=0 is the worst possible.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 January 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of values.
#
#    Input, real Y_DATA(N), Y_MODEL(N), the data and model values.
#
#    Output, real R8VEC_RSQUARED, the R^2 value.
#
  import numpy as np

  y_average = np.sum ( y_data[0:n] ) / n

  top = np.sum ( ( y_data[0:n] - y_model[0:n] ) ** 2 )
  bot = np.sum ( ( y_data[0:n] - y_average ) ** 2 )

  value = 1.0 - top / bot

  return value

def r8vec_rsquared_test ( ):

#*****************************************************************************80
#
## R8VEC_RSQUARED_TEST tests R8VEC_RSQUARED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 January 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec2_print import r8vec2_print

  print ( '' )
  print ( 'R8VEC_RSQUARED_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_RSQUARED computes the R^2 goodness-of-fit statistic.' )

  n = 11

  y_model = np.array ( [ \
     0.00,  9.00, 16.00, 21.00, 24.00, \
    25.00, 24.00, 21.00, 16.00,  9.00,  \
     0.00 ] )
  y_data = np.array ( [ \
     0.00,  9.58, 16.76, 21.52, 24.38, \
    24.97, 22.90, 20.45, 12.40,  7.65, \
    -3.82 ] )

  r8vec2_print ( n, y_data, y_model, "  Data and model:" )

  rsquared = r8vec_rsquared ( n, y_data, y_model )
  print ( '' )
  print ( '  Computed R^2 is %g' % ( rsquared ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_RSQUARED_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_rsquared_test ( )
  timestamp ( )

