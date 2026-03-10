#! /usr/bin/env python3
#
def graphviz_test ( ):

#*****************************************************************************80
#
## graphviz_test() tests graphviz().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 May 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'graphviz_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test graphviz().' )

  from alphabet_binary_tree         import alphabet_binary_tree
  from network_graph                import network_graph
  from web_digraph                  import web_digraph

  alphabet_binary_tree ( )
  network_graph ( )
  web_digraph ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'graphviz_test:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  graphviz_test ( )
  timestamp ( )
 
