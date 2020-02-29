#  spiral_data_commands.txt
#
set term png
set output "spiral_data.png"
#
#  Add titles and labels.
#
set xlabel "<--- X --->"
set ylabel "<--- Y --->"
set title "Spiral velocity flow"
unset key
#
#  Add grid lines.
#
set grid
set size ratio -1
#
#  Timestamp the plot.
#
set timestamp
plot "spiral_data_data.txt" using 1:2:3:4 with vectors \
  head filled lt 2 linecolor rgb "blue"
quit
