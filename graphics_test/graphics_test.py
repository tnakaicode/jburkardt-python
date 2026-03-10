#! /usr/bin/env python3
#
def graphics_test ( ):

#*****************************************************************************80
#
## graphics_test() tests the graphics examples.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 April 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'graphics_test():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Test the graphics examples.' )

  from album_bar                    import album_bar
  from alphabet_binary_tree         import alphabet_binary_tree
  from automobile_scatter           import automobile_scatter
  from basketball_barh              import basketball_barh
  from brownian_2d_plot             import brownian_2d_plot
  from brownian_animation           import brownian_animation
  from bulgaria_plot                import bulgaria_plot
  from caffeine_scatter             import caffeine_scatter
  from chain_letter_dendrogram      import chain_letter_dendrogram
  from circle_scatters              import circle_scatters
  from corkscrew_plot3d             import corkscrew_plot3d
  from correlation_heat_map         import correlation_heat_map
  from corvette_scatter             import corvette_scatter
  from drug_dosage_plots            import drug_dosage_plots
  from flow_vector                  import flow_vector
  from genealogy_tree               import genealogy_tree
  from geyser_bar                   import geyser_bar
  from geyser_histogram             import geyser_histogram
  from geyser_scatter               import geyser_scatter
  from gradient_vector              import gradient_vector
  from grid_fill_contour            import grid_fill_contour
  from grid_surface                 import grid_surface
  from insect_scatter3d             import insect_scatter3d
  from integral_between             import integral_between
  from iris_decision_tree           import iris_decision_tree
  from iris_subplots                import iris_subplots
  from knight_graph                 import knight_graph
  from least_squares_plots          import least_squares_plots
  from lissajous_plot               import lissajous_plot
  from lynx_plot                    import lynx_plot
  from mario_fill                   import mario_fill
  from mod_bar3d                    import mod_bar3d
  from network_graph                import network_graph
  from nile_histogram               import nile_histogram
  from nile_plot                    import nile_plot
  from ninety_histogram             import ninety_histogram
  from orbital_fill_contour         import orbital_fill_contour
  from polygon_fill                 import polygon_fill
  from predator_plot3d              import predator_plot3d
  from president_heights_bar        import president_heights_bar
  from president_heights_barh       import president_heights_barh
  from president_heights_histogram  import president_heights_histogram
  from price_plots                  import price_plots
  from random_scatter               import random_scatter
  from schoolyear_barh              import schoolyear_barh
  from snowfall_histogram           import snowfall_histogram
  from snowfall_plot                import snowfall_plot
  from snowfall_smoothed_plot       import snowfall_smoothed_plot
  from sombrero_surface             import sombrero_surface
  from temperature_scatter          import temperature_scatter
  from temperature_scatter3d        import temperature_scatter3d
  from track_bar                    import track_bar
  from volcano_fill_contour         import volcano_fill_contour
  from volcano_line_contour         import volcano_line_contour
  from volcano_surface              import volcano_surface
  from web_digraph                  import web_digraph

  album_bar ( )
  alphabet_binary_tree ( )
  automobile_scatter ( )
  basketball_barh ( )
  brownian_2d_plot ( )
  brownian_animation ( )
  bulgaria_plot ( )
  caffeine_scatter ( )
  chain_letter_dendrogram ( )
  circle_scatters ( )
  corkscrew_plot3d ( )
  correlation_heat_map ( )
  corvette_scatter ( )
  drug_dosage_plots ( )
  flow_vector ( )
  genealogy_tree ( )
  geyser_bar ( )
  geyser_histogram ( )
  geyser_scatter ( )
  gradient_vector ( )
  grid_fill_contour ( )
  grid_surface ( )
  insect_scatter3d ( )
  integral_between ( )
  iris_decision_tree ( )
  iris_subplots ( )
  knight_graph ( )
  least_squares_plots ( )
  lissajous_plot ( )
  lynx_plot ( )
  mario_fill ( )
  mod_bar3d ( )
  network_graph ( )
  nile_histogram ( )
  nile_plot ( )
  ninety_histogram ( )
  orbital_fill_contour ( )
  polygon_fill ( )
  predator_plot3d ( )
  president_heights_bar ( )
  president_heights_barh ( )
  president_heights_histogram ( )
  price_plots ( )
  random_scatter ( )
  schoolyear_barh ( )
  snowfall_histogram ( )
  snowfall_plot ( )
  snowfall_smoothed_plot ( )
  sombrero_surface ( )
  temperature_scatter ( )
  temperature_scatter3d ( )
  track_bar ( )
  volcano_fill_contour ( )
  volcano_line_contour ( )
  volcano_surface ( )
  web_digraph ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'graphics_test():' )
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

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  graphics_test ( )
  timestamp ( )
 
