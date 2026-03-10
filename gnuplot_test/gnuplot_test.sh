#! /bin/bash
#
python3 gnuplot_test.py > gnuplot_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
gnuplot < damped_sine_commands.txt
rm damped_sine_commands.txt
rm damped_sine_data.txt
#
gnuplot < mark_points_commands.txt
rm mark_points_commands.txt
rm mark_points_data.txt
rm mark_points_start_data.txt
rm mark_points_end_data.txt
#
gnuplot < orbital_fill_contour_commands.txt
rm orbital_fill_contour_commands.txt
#
gnuplot < string_simulation_commands.txt
rm string_simulation_commands.txt
rm string_simulation_data.txt
#
#  Get rid of obnoxious garbage.
#
rm -f *.pyc
rm -rf __pycache__
#
echo "Normal end of execution."
