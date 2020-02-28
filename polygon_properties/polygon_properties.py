#! /usr/bin/env python3
#
def polygon_properties_test ( ):

#*****************************************************************************80
#
## POLYGON_PROPERTIES_TEST tests the POLYGON_PROPERTIES library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 October 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from polygon_angles             import polygon_angles_test
  from polygon_area               import polygon_area_test
  from polygon_area_2             import polygon_area_2_test
  from polygon_centroid           import polygon_centroid_test
  from polygon_centroid_2         import polygon_centroid_2_test
  from polygon_contains_point     import polygon_contains_point_test
  from polygon_contains_point_2   import polygon_contains_point_2_test
  from polygon_diameter           import polygon_diameter_test
  from polygon_expand             import polygon_expand_test
  from polygon_inrad_data         import polygon_inrad_data_test
  from polygon_integral_1         import polygon_integral_1_test
  from polygon_integral_x         import polygon_integral_x_test
  from polygon_integral_xx        import polygon_integral_xx_test
  from polygon_integral_xy        import polygon_integral_xy_test
  from polygon_integral_y         import polygon_integral_y_test
  from polygon_integral_yy        import polygon_integral_yy_test
  from polygon_is_convex          import polygon_is_convex_test
  from polygon_lattice_area       import polygon_lattice_area_test
  from polygon_outrad_data        import polygon_outrad_data_test
  from polygon_perimeter          import polygon_perimeter_test
  from polygon_perimeter_quad     import polygon_perimeter_quad_test
  from polygon_point_dist         import polygon_point_dist_test
  from polygon_point_near         import polygon_point_near_test
  from polygon_sample             import polygon_sample_test
  from polygon_side_data          import polygon_side_data_test
  from polygon_triangulate        import polygon_triangulate_test

  print ( '' )
  print ( 'POLYGON_PROPERTIES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the POLYGON_PROPERTIES library.' )

  polygon_angles_test ( )
  polygon_area_test ( )
  polygon_area_2_test ( )
  polygon_centroid_test ( )
  polygon_centroid_2_test ( )
  polygon_contains_point_test ( )
  polygon_contains_point_2_test ( )
  polygon_diameter_test ( )
  polygon_expand_test ( )
  polygon_inrad_data_test ( )
  polygon_integral_1_test ( )
  polygon_integral_x_test ( )
  polygon_integral_xx_test ( )
  polygon_integral_xy_test ( )
  polygon_integral_y_test ( )
  polygon_integral_yy_test ( )
  polygon_is_convex_test ( )
  polygon_lattice_area_test ( )
  polygon_outrad_data_test ( )
  polygon_perimeter_test ( )
  polygon_perimeter_quad_test ( )
  polygon_point_dist_test ( )
  polygon_point_near_test ( )
  polygon_sample_test ( )
  polygon_side_data_test ( )
  polygon_triangulate_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_PROPERTIES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_properties_test ( )
  timestamp ( )
