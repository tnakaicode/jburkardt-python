#! /usr/bin/env python3
#
def sympy_plot ( ):

#*****************************************************************************80
#
## sympy_plot() uses sympy() to make plots.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 August 2024
#
#  Author:
#
#    John Burkardt
#
  from sympy import symbols
  from sympy.plotting import plot

  print ( '' )
  print ( 'sympy_plot():' )
  print ( '  Plot the humps() function over 0 <= x <= 2.' )

  x = symbols ( 'x' )

# humps = 1 / ( ( x - 3 / 10 )**2 + 1 / 100 ) \
#       + 1 / ( ( x - 9 / 10 )**2 + 4 / 100 ) \
#       - 6
  humps = 100 / ( ( 10 * x - 3 )**2 + 1 ) \
        + 100 / ( ( 10 * x - 9 )**2 + 4 ) \
        - 6

  p = plot ( humps, ( x, 0, 2 ), show = False )
  filename = 'sympy_plot.png'
  p.save ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

if ( __name__ == "__main__" ):
  sympy_plot ( )

