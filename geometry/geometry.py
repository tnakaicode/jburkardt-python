#! /usr/bin/env python3
#
def geometry_test ( ):

#*****************************************************************************80
#
## GEOMETRY_TEST tests the GEOMETRY library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 August 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  from angle_degree                    import angle_degree_test
  from angle_half                      import angle_half_test
  from angle_radian                    import angle_radian_test

  from ball01_volume                   import ball01_volume_test

  from circle_area                     import circle_area_test
  from circle_imp_point_dist_2d        import circle_imp_point_dist_2d_test
  from circle_imp_print_2d             import circle_imp_print_2d_test
  from circle_lune_angle_by_height_2d  import circle_lune_angle_by_height_2d_test
  from circle_lune_area_by_angle_2d    import circle_lune_area_by_angle_2d_test
  from circle_lune_area_by_height_2d   import circle_lune_area_by_height_2d_test
  from circle_lune_height_by_angle_2d  import circle_lune_height_by_angle_2d_test
  from circle_sector_area_2d           import circle_sector_area_2d_test
  from circle_triangle_area_2d         import circle_triangle_area_2d_test

  from circle01_length                 import circle01_length_test        

  from circles_intersect_area_2d       import circles_intersect_area_2d_test
  from circles_intersect_points_2d     import circles_intersect_points_2d_test

  from cone_volume                     import cone_volume_test

  from cube01_volume                   import cube01_volume_test

  from degrees_to_radians              import degrees_to_radians_test

  from disk01_area                     import disk01_area_test

  from disk01_quarter_area             import disk01_quarter_area_test

  from ellipse_area1                   import ellipse_area1_test
  from ellipse_area2                   import ellipse_area2_test
  from ellipse_area3                   import ellipse_area3_test
  from ellipse_point_near              import ellipse_point_near_test

  from ellipsoid_volume                import ellipsoid_volume_test

  from hyperball01_volume              import hyperball01_volume_test

  from hypercube01_volume              import hypercube01_volume_test

  from hypersphere01_area              import hypersphere01_area_test

  from i4_modp                         import i4_modp_test
  from i4_wrap                         import i4_wrap_test

  from line_exp2imp                    import line_exp2imp_test
  from line_exp_perp                   import line_exp_perp_test
  from line_imp2exp                    import line_imp2exp_test

  from lines_exp_int                   import lines_exp_int_test
  from lines_imp_int                   import lines_imp_int_test

  from polygon_angles                  import polygon_angles_test
  from polygon_area                    import polygon_area_test
  from polygon_area_2                  import polygon_area_2_test
  from polygon_centroid                import polygon_centroid_test
  from polygon_centroid_2              import polygon_centroid_2_test
  from polygon_contains_point          import polygon_contains_point_test
  from polygon_contains_point_2        import polygon_contains_point_2_test
  from polygon_diameter                import polygon_diameter_test
  from polygon_expand                  import polygon_expand_test
  from polygon_inrad_data              import polygon_inrad_data_test
  from polygon_integral_1              import polygon_integral_1_test
  from polygon_integral_x              import polygon_integral_x_test
  from polygon_integral_xx             import polygon_integral_xx_test
  from polygon_integral_xy             import polygon_integral_xy_test
  from polygon_integral_y              import polygon_integral_y_test
  from polygon_integral_yy             import polygon_integral_yy_test
  from polygon_is_convex               import polygon_is_convex_test
  from polygon_lattice_area            import polygon_lattice_area_test
  from polygon_outrad_data             import polygon_outrad_data_test
  from polygon_perimeter               import polygon_perimeter_test
  from polygon_perimeter_quad          import polygon_perimeter_quad_test
  from polygon_point_dist              import polygon_point_dist_test
  from polygon_point_near              import polygon_point_near_test
  from polygon_side_data               import polygon_side_data_test
  from polygon_triangulate             import polygon_triangulate_test

  from pyramid_volume                  import pyramid_volume_test
  from pyramid01_volume                import pyramid01_volume_test

  from r8_acos                         import r8_acos_test
  from r8_atan                         import r8_atan_test
  from r8_sign                         import r8_sign_test
  from r8_uniform_01                   import r8_uniform_01_test
  from r8_uniform_ab                   import r8_uniform_ab_test

  from r8mat_det_4d                    import r8mat_det_4d_test
  from r8mat_print                     import r8mat_print_test
  from r8mat_print_some                import r8mat_print_some_test
  from r8mat_solve                     import r8mat_solve_test
  from r8mat_transpose_print           import r8mat_transpose_print_test
  from r8mat_transpose_print_some      import r8mat_transpose_print_some_test

  from r8vec_print                     import r8vec_print_test
  from r8vec_transpose_print           import r8vec_transpose_print_test
  from r8vec_uniform_01                import r8vec_uniform_01_test
  from r8vec_uniform_ab                import r8vec_uniform_ab_test

  from r8vec2_print                    import r8vec2_print_test

  from r8vec3_print                    import r8vec3_print_test

  from radians_to_degrees              import radians_to_degrees_test

  from segment_point_dist              import segment_point_dist_test
  from segment_point_near              import segment_point_near_test

  from simplex01_volume                import simplex01_volume_test

  from sphere_triangle_sides_to_angles import sphere_triangle_sides_to_angles_test

  from sphere01_area                   import sphere01_area_test
  from sphere01_area_values            import sphere01_area_values_test
  from sphere01_volume_values          import sphere01_volume_values_test

  from tetrahedron_barycentric         import tetrahedron_barycentric_test
  from tetrahedron_centroid            import tetrahedron_centroid_test
  from tetrahedron_sample              import tetrahedron_sample_test
  from tetrahedron_volume              import tetrahedron_volume_test

  from tetrahedron01_volume            import tetrahedron01_volume_test

  from triangle_angles                 import triangle_angles_test
  from triangle_area                   import triangle_area_test
  from triangle_barycentric            import triangle_barycentric_test
  from triangle_centroid               import triangle_centroid_test
  from triangle_circumcircle           import triangle_circumcircle_test
  from triangle_contains_point         import triangle_contains_point_test
  from triangle_contains_point_1       import triangle_contains_point_1_test
  from triangle_diameter               import triangle_diameter_test
  from triangle_edge_length            import triangle_edge_length_test
  from triangle_incircle               import triangle_incircle_test
  from triangle_orientation            import triangle_orientation_test
  from triangle_orthocenter            import triangle_orthocenter_test
  from triangle_point_dist             import triangle_point_dist_test
  from triangle_point_near             import triangle_point_near_test
  from triangle_quality                import triangle_quality_test
  from triangle_reference_sample       import triangle_reference_sample_test
  from triangle_sample                 import triangle_sample_test
  from triangle_xsi_to_xy              import triangle_xsi_to_xy_test
  from triangle_xy_to_xsi              import triangle_xy_to_xsi_test

  from triangle01_area                 import triangle01_area_test
  from triangle01_sample               import triangle01_sample_test

  from wedge01_volume                  import wedge01_volume_test

  print ( '' )
  print ( 'GEOMETRY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the GEOMETRY library.' )

  angle_degree_test ( )
  angle_half_test ( )
  angle_radian_test ( )

  ball01_volume_test ( )

  circle_area_test ( )
  circle_imp_point_dist_2d_test ( )
  circle_imp_print_2d_test ( )
  circle_lune_angle_by_height_2d_test ( )
  circle_lune_area_by_angle_2d_test ( )
  circle_lune_area_by_height_2d_test ( )
  circle_lune_height_by_angle_2d_test ( )
  circle_sector_area_2d_test ( )
  circle_triangle_area_2d_test ( )

  circle01_length_test ( )

  circles_intersect_area_2d_test ( )
  circles_intersect_points_2d_test ( )

  cone_volume_test ( )

  cube01_volume_test ( )

  degrees_to_radians_test ( )

  disk01_area_test ( )

  disk01_quarter_area_test ( )

  ellipse_area1_test ( )
  ellipse_area2_test ( )
  ellipse_area3_test ( )
  ellipse_point_near_test ( )

  ellipsoid_volume_test ( )

  hyperball01_volume_test ( )

  hypercube01_volume_test ( )

  hypersphere01_area_test ( )

  i4_modp_test ( )
  i4_wrap_test ( )

  line_exp2imp_test ( )
  line_exp_perp_test ( )

  lines_exp_int_test ( )
  lines_imp_int_test ( )

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
  polygon_side_data_test ( )
  polygon_triangulate_test ( )

  pyramid_volume_test ( )
  pyramid01_volume_test ( )

  r8_acos_test ( )
  r8_atan_test ( )
  r8_sign_test ( )
  r8_uniform_01_test ( )
  r8_uniform_ab_test ( )

  r8mat_det_4d_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_solve_test ( )
  r8mat_transpose_print_test ( )
  r8mat_transpose_print_some_test ( )

  r8vec_print_test ( )
  r8vec_transpose_print_test ( )
  r8vec_uniform_01_test ( )
  r8vec_uniform_ab_test ( )

  r8vec2_print_test ( )

  r8vec3_print_test ( )

  radians_to_degrees_test ( )

  segment_point_dist_test ( )
  segment_point_near_test ( )

  simplex01_volume_test ( )

  sphere_triangle_sides_to_angles_test ( )

  sphere01_area_test ( )
  sphere01_area_values_test ( )
  sphere01_volume_values_test ( )

  tetrahedron_barycentric_test ( )
  tetrahedron_centroid_test ( )
  tetrahedron_sample_test ( )
  tetrahedron_volume_test ( )

  tetrahedron01_volume_test ( )

  triangle_angles_test ( )
  triangle_area_test ( )
  triangle_barycentric_test ( )
  triangle_centroid_test ( )
  triangle_circumcircle_test ( )
  triangle_contains_point_test ( )
  triangle_contains_point_1_test ( )
  triangle_diameter_test ( )
  triangle_edge_length_test ( )
  triangle_incircle_test ( )
  triangle_orientation_test ( )
  triangle_orthocenter_test ( )
  triangle_point_dist_test ( )
  triangle_point_near_test ( )
  triangle_quality_test ( )
  triangle_reference_sample_test ( )
  triangle_sample_test ( )
  triangle_xsi_to_xy_test ( )
  triangle_xy_to_xsi_test ( )

  triangle01_area_test ( )
  triangle01_sample_test ( )

  wedge01_volume_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'GEOMETRY_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp     import timestamp
  timestamp ( )
  geometry_test ( )
  timestamp ( )
