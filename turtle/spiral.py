#! /usr/bin/env python3
#
def spiral ( ):

  from PIL import Image
  import turtle

  window = turtle.Screen ( )
  window.bgcolor ( "lightgreen" )
  canvas = window.getcanvas ( )

  tess = turtle.Turtle ( )
  tess.shape ( "turtle" )
  tess.color ( "blue" )

  tess.penup ( )
  size = 20
  for i in range ( 30 ):
    tess.stamp ( )
    size = size + 3
    tess.forward ( size )
    tess.right ( 24 )

  canvas.postscript ( file = "spiral.eps" )
  fred = Image.open ( "spiral.eps" )
  fred.save ( "spiral.png", "PNG" )

  window.mainloop ( )

  return

if ( __name__ == "__main__" ):
  spiral ( )

