#! /usr/bin/env python3
#
from turtle import *

def example ( ):

  from PIL import Image

  import turtle

  screen = turtle.Screen ( )
  canvas = screen.getcanvas ( )

  t = Turtle ( )

  t.screen.title ( 'Turtle graphics example' )

  color ( 'green' )
  right ( 45 )
  forward ( 300 )
  stamp ( )
  left ( 120 )
  forward ( 100 )
  color('red')
  right ( 30 )
  backward ( 450 )
  width(3)
  left(50)
  forward(50)
  pos ( )
#
#  Draw a filled star
#
  home ( )
  color('blue')
  fillcolor('yellow')
  begin_fill()
  while True:
    forward(200)
    left(130)
    if abs ( pos() ) < 1:
      break
  end_fill ( )
#
#  Don't close the window right away.
#
  canvas.postscript ( file = "my_drawing.eps" )
  Image.open("my_drawing.eps").save("my_drawing.png", "PNG")

  t.screen.mainloop ( )

  return

if ( __name__ == "__main__" ):
  example ( )

