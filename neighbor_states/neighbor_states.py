#! /usr/bin/env python3
#
def neighbor_states ( ):

#*****************************************************************************80
#
## neighbor_states() plots the US states using only neighbor information.
#
#  Discussion:
#
#    To use this example, you need to have installed graphviz and pydotplus.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 November 2022
#
#  Author:
#
#    John Burkardt
#
  import graphviz
  import numpy as np
  import platform

  print ( '' )
  print ( 'neighbor_states():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Plot the US states, using only neighor information.' )
  print ( '' )

  plot = graphviz.Graph ( comment = 'The US States', format = 'png', engine = 'neato' )
#
#  Specify the nodes, giving each an internal code, and a label.
#
  for i in range ( 0, 50 ):
    state_code = str ( i )
    state_id = state_id_from_index ( i )
    plot.node ( state_code, state_id ) 
    print ( state_code, state_id )
#
#  Specify the edges as connections between two nodes.
#
  st = state_neighbors ( )

  for s, t in st:
    if ( s < t ):
      state_code_s = str ( s - 1 )
      state_code_t = str ( t - 1)
      plot.edge ( state_code_s, state_code_t )

  plot.layout = 'circo'

  print ( plot.source )
#
#  Save graph to a file, and optionally display an image to the screen.
#
# plot.render ( 'neighbor_states.plot', view = False )
# plot.render ( 'neighbor_states.dot', view = False )
  plot.render ( 'neighbor_states', view = False )

# filename = 'neighbor_states.plot.png'
  filename = 'neighbor_states.png'
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'neighbor_states():' )
  print ( '  Normal end of execution.' )
  return

def state_id_from_index ( index ):

#*****************************************************************************80
#
## state_id_from_index() returns the ID of a given US state.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer index: the state index, between 1 and 50.
#
#  Output:
#
#    character id: the state ID.  
#
  state_id = [ \
    'AL', \
    'AK', \
    'AZ', \
    'AR', \
    'CA', \
    'CO', \
    'CT', \
    'DE', \
    'FL', \
    'GA', \
    'HI', \
    'ID', \
    'IL', \
    'IN', \
    'IA', \
    'KS', \
    'KY', \
    'LA', \
    'ME', \
    'MD', \
    'MA', \
    'MI', \
    'MN', \
    'MS', \
    'MO', \
    'MT', \
    'NE', \
    'NV', \
    'NH', \
    'NJ', \
    'NM', \
    'NY', \
    'NC', \
    'ND', \
    'OH', \
    'OK', \
    'OR', \
    'PA', \
    'RI', \
    'SC', \
    'SD', \
    'TN', \
    'TX', \
    'UT', \
    'VT', \
    'VA', \
    'WA', \
    'WV', \
    'WI', \
    'WY' ]

  return state_id[index]

def state_neighbors ( ):

#*****************************************************************************80
#
## state_neighbors() returns an array of pairs of US state neighbors.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer st(210,2): the indices of pairs of state neighbors. 
#
  import numpy as np

  st = np.array ( [ \
    [ 1,9 ], \
    [ 1,10 ], \
    [ 1,42 ], \
    [ 1,24 ], \
    [ 3,31 ], \
    [ 3,44 ], \
    [ 3,28 ], \
    [ 3,5 ], \
    [ 4,18 ], \
    [ 4,24 ], \
    [ 4,42 ], \
    [ 4,25 ], \
    [ 4,36 ], \
    [ 4,43 ], \
    [ 5,3 ], \
    [ 5,28 ], \
    [ 5,37 ], \
    [ 6,31 ], \
    [ 6,36 ], \
    [ 6,16 ], \
    [ 6,27 ], \
    [ 6,50 ], \
    [ 6,44 ], \
    [ 7,39 ], \
    [ 7,21 ], \
    [ 7,32 ], \
    [ 8,30 ], \
    [ 8,38 ], \
    [ 8,20 ], \
    [ 9,10 ], \
    [ 9,1 ], \
    [ 10,40 ], \
    [ 10,33 ], \
    [ 10,42 ], \
    [ 10,1 ], \
    [ 10,9 ], \
    [ 12,47 ], \
    [ 12,37 ], \
    [ 12,28 ], \
    [ 12,44 ], \
    [ 12,50 ], \
    [ 12,26 ], \
    [ 13,49 ], \
    [ 13,15 ], \
    [ 13,25 ], \
    [ 13,17 ], \
    [ 13,14 ], \
    [ 14,13 ], \
    [ 14,17 ], \
    [ 14,35 ], \
    [ 14,22 ], \
    [ 15,23 ], \
    [ 15,41 ], \
    [ 15,27 ], \
    [ 15,25 ], \
    [ 15,13 ], \
    [ 15,49 ], \
    [ 16,36 ], \
    [ 16,25 ], \
    [ 16,27 ], \
    [ 16,6 ], \
    [ 17,42 ], \
    [ 17,46 ], \
    [ 17,48 ], \
    [ 17,35 ], \
    [ 17,14 ], \
    [ 17,13 ], \
    [ 17,25 ], \
    [ 18,24 ], \
    [ 18,4 ], \
    [ 18,43 ], \
    [ 19,29 ], \
    [ 20,8 ], \
    [ 20,38 ], \
    [ 20,48 ], \
    [ 20,46 ], \
    [ 21,29 ], \
    [ 21,45 ], \
    [ 21,32 ], \
    [ 21,7 ], \
    [ 21,39 ], \
    [ 22,49 ], \
    [ 22,14 ], \
    [ 22,35 ], \
    [ 23,34 ], \
    [ 23,41 ], \
    [ 23,15 ], \
    [ 23,49 ], \
    [ 24,1 ], \
    [ 24,42 ], \
    [ 24,4 ], \
    [ 24,18 ], \
    [ 25,4 ], \
    [ 25,42 ], \
    [ 25,17 ], \
    [ 25,13 ], \
    [ 25,15 ], \
    [ 25,27 ], \
    [ 25,16 ], \
    [ 25,36 ], \
    [ 26,12 ], \
    [ 26,50 ], \
    [ 26,41 ], \
    [ 26,34 ], \
    [ 27,16 ], \
    [ 27,25 ], \
    [ 27,15 ], \
    [ 27,41 ], \
    [ 27,50 ], \
    [ 27,6 ], \
    [ 28,3 ], \
    [ 28,44 ], \
    [ 28,12 ], \
    [ 28,37 ], \
    [ 28,5 ], \
    [ 29,45 ], \
    [ 29,21 ], \
    [ 29,19 ], \
    [ 30,32 ], \
    [ 30,38 ], \
    [ 30,8 ], \
    [ 31,43 ], \
    [ 31,36 ], \
    [ 31,6 ], \
    [ 31,3 ], \
    [ 32,38 ], \
    [ 32,30 ], \
    [ 32,7 ], \
    [ 32,21 ], \
    [ 32,45 ], \
    [ 33,46 ], \
    [ 33,42 ], \
    [ 33,10 ], \
    [ 33,40 ], \
    [ 34,26 ], \
    [ 34,41 ], \
    [ 34,23 ], \
    [ 35,22 ], \
    [ 35,14 ], \
    [ 35,17 ], \
    [ 35,48 ], \
    [ 35,38 ], \
    [ 36,43 ], \
    [ 36,4 ], \
    [ 36,25 ], \
    [ 36,16 ], \
    [ 36,6 ], \
    [ 36,31 ], \
    [ 37,5 ], \
    [ 37,28 ], \
    [ 37,12 ], \
    [ 37,47 ], \
    [ 38,35 ], \
    [ 38,48 ], \
    [ 38,20 ], \
    [ 38,8 ], \
    [ 38,30 ], \
    [ 38,32 ], \
    [ 39,21 ], \
    [ 39,7 ], \
    [ 40,33 ], \
    [ 40,10 ], \
    [ 41,27 ], \
    [ 41,15 ], \
    [ 41,23 ], \
    [ 41,34 ], \
    [ 41,26 ], \
    [ 41,50 ], \
    [ 42,1 ], \
    [ 42,10 ], \
    [ 42,33 ], \
    [ 42,46 ], \
    [ 42,17 ], \
    [ 42,25 ], \
    [ 42,4 ], \
    [ 42,24 ], \
    [ 43,18 ], \
    [ 43,4 ], \
    [ 43,36 ], \
    [ 43,31 ], \
    [ 44,3 ], \
    [ 44,6 ], \
    [ 44,50 ], \
    [ 44,12 ], \
    [ 44,28 ], \
    [ 45,32 ], \
    [ 45,21 ], \
    [ 45,29 ], \
    [ 46,20 ], \
    [ 46,48 ], \
    [ 46,17 ], \
    [ 46,42 ], \
    [ 46,33 ], \
    [ 47,37 ], \
    [ 47,12 ], \
    [ 48,46 ], \
    [ 48,20 ], \
    [ 48,38 ], \
    [ 48,35 ], \
    [ 48,17 ], \
    [ 49,23 ], \
    [ 49,15 ], \
    [ 49,13 ], \
    [ 49,22 ], \
    [ 50,6 ], \
    [ 50,27 ], \
    [ 50,41 ], \
    [ 50,26 ], \
    [ 50,12 ], \
    [ 50,44 ] ] )

  return st
    
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
  neighbor_states ( )
  timestamp ( )

