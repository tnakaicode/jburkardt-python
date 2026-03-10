#! /usr/bin/env python3
#
def cursor_test():

# importing cursor widget from matplotlib
#
  from matplotlib.widgets import Cursor
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '\n' );
  print ( 'cursor_test():\n' );
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )

  rng = default_rng ( )

  fig = plt.figure()
  ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
  
  num = 100
  x = rng.random ( size = num )
  y = rng.random ( size = num )
  
  ax.scatter(x, y, c='blue')
  ax.set_xlabel('X-axis')
  ax.set_ylabel('Y-axis')
  
  cursor = Cursor ( ax, color = 'green', linewidth = 2, \
    horizon = False, verton = True, useblit = True )

  #plt.show()

  coord = []

  def onclick(event):
    global coord
    coord.append((event.xdata, event.ydata))
    x = event.xdata
    y = event.ydata
    
    # printing the values of the selected point
    print([x,y]) 
#   annot.xy = (x,y)
#   text = "({:.2g}, {:.2g})".format(x,y)
#   annot.set_text(text)
#   annot.set_visible(True)
    fig.canvas.draw() #redraw the figure
    
  fig.canvas.mpl_connect('button_press_event', onclick)
  plt.show()

  return

if ( __name__ == "__main__" ):
  cursor_test ( )

