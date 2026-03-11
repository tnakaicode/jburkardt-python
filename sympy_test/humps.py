def humps_fun ( x ):

#*****************************************************************************80
#
## humps_fun() evaluates the humps function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x(): the evaluation points.
#
#  Output:
#
#    real y(): the function values.
#
  humps = 100 / ( ( 10 * x - 3 )**2 + 1 ) \
        + 100 / ( ( 10 * x - 9 )**2 + 4 ) \
        - 6

  return humps

