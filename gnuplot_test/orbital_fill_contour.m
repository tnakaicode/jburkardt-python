def orbital_fill_contour ( ):

#*****************************************************************************80
#
## orbital_fill_contour() creates a color contour plot of orbital data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'orbital_fill_contour():' )
  print ( '  Color contour plot of orbital data using gnuplot().' )

  command_filename = 'orbital_fill_contour_commands.txt'
  command_unit = fopen ( command_filename, 'wt' )
  fprintf ( command_unit, '# #s', command_filename )
  fprintf ( command_unit, '#' )
  fprintf ( command_unit, '# Usage:' )
  fprintf ( command_unit, '#  gnuplot < #s', command_filename )
  fprintf ( command_unit, '#' )
  fprintf ( command_unit, 'set term png' )
  fprintf ( command_unit, 'set output "orbital_fill_contour.png"' )
  fprintf ( command_unit, 'set xlabel "<--- X --->"' )
  fprintf ( command_unit, 'set ylabel "<--- Y --->"' )
  fprintf ( command_unit, 'set title "Orbital Data"' )
  fprintf ( command_unit, 'set grid' )
  fprintf ( command_unit, 'unset surface' )
  fprintf ( command_unit, 'set contour base' )
  fprintf ( command_unit, 'set view map' )
  fprintf ( command_unit, 'set pm3d' )
  fprintf ( command_unit, 'splot "orbital_gnuplot_data.txt" with pm3d' )
  fprintf ( command_unit, 'quit' )
  fclose ( command_unit )
  print ( '  Created command file "#s"', command_filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'orbital_fill_contour():' )
  print ( '  Normal end of execution.' )

  return
end

