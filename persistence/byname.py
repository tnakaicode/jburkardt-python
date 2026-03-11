#! /usr/bin/env python3
#
def byname ( action = None, name = None, value_in = None ):

#*****************************************************************************80
#
## byname() controls a set of named persistent data.
#
#  Discussion:
#
#    Three values are stored, named ALPHA, BETA and GAMMA.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string ACTION (case insensitive, only first character important)
#    "Get"     get the value
#    "Print"   print the value
#    "Reset"   reset value to default
#    "Set"     set the value
#
#    string NAME, the name of the parameter (case insensitive)
#    "ALPHA"
#    "BETA"
#    "GAMMA"
#    "*" (all variables)
#    NAME is required for "Get" and "Set".  
#    NAME, if omitted, is assumed "*" for "Print" and "Reset".
#
#    VALUE_IN.
#    Only used for "Set" command.
#
#  Output:
#
#    VALUE_OUT.
#    If NAME was specified on input, and was not "*", then
#    VALUE_OUT is the current value of the corresponding variable.
#    Otherwise, VALUE_OUT is empty.
#
  if not hasattr ( byname, "alpha" ):
    byname.alpha = 1.0

  if not hasattr ( byname, "alpha_default" ):
    byname.alpha_default = 1.0

  if not hasattr ( byname, "beta" ):
    byname.beta = 2.0

  if not hasattr ( byname, "beta_default" ):
    byname.beta_default = 2.0

  if not hasattr ( byname, "gamma" ):
    byname.gamma = 3.0

  if not hasattr ( byname, "gamma_default" ):
    byname.gamma_default = 3.0
#
#  Process "action":
#
  if ( action is None ):
    action2 = "p"
  else:
    action2 = action[0]
    action2 = action2.lower()
    match = \
      ( action2 == "g" ) or \
      ( action2 == "p" ) or \
      ( action2 == "r" ) or \
      ( action2 == "s" ) 

    if ( not match ):
      print ( '' )
      print ( 'byname(): Fatal error!' )
      print ( '  Legal actions are "g", "p", "r", "s"' )
      print ( '  Not "', action, '"' )
      raise Exception ( 'byname(): Fatal error!' )
#
#  Process "name"
#
  if ( ( action2 == "p" or action2 == "r" ) and name is None ):
    name2 = "*"
  else:
    name2 = name[0]
    name2 = name2.lower()
    match = \
      ( name2 == "a" ) or \
      ( name2 == "b" ) or \
      ( name2 == "g" ) or \
      ( name2 == "*" ) 

    if ( not match ):
      print ( '' )
      print ( 'byname: Fatal error!' )
      print ( '  Legal names are "alpha", "beta", "gamma", "*"' )
      print ( '  Not "', name , '".' )
      raise Exception ( 'byname(): Fatal error!' )
#
#  Reject missing value.
#
  if ( action2 == "s" and value_in is None ):
    print ( '' )
    print ( 'byname: Fatal error!' )
    print ( '  "set, name" command but no "value".' )
    raise Exception ( 'byname(): Fatal error!' )
#
#  Carry out requested action.
#
  value_out = None

  if ( action2 == "g" ):
    if ( name2 == "a" ):
      value_out = byname.alpha
    elif ( name2 == "b" ):
      value_out = byname.beta
    elif ( name2 == "g" ):
      value_out = byname.gamma
  elif ( action2 == "p" ):
    if ( name2 == "a" or name2 == "*" ):
      print ( '  alpha = ', byname.alpha )
    if ( name2 == "a" ):
      value_out = byname.alpha
    if ( name2 == "b" or name2 == "*" ):
      print ( '  beta  = ', byname.beta )
    if ( name2 == "b" ):
      value_out = byname.beta
    if ( name2 == "g" or name2 == "*" ):
      print ( '  gamma = ', byname.gamma )
    if ( name2 == "g" ):
      value_out = byname.gamma
  elif ( action2 == "r" ):
    if ( name2 == "a" or name2 == "*" ):
      byname.alpha = byname.alpha_default
    if ( name2 == "a" ):
      value_out = byname.alpha
    if ( name2 == "b" or name2 == "*" ):
      byname.beta = byname.beta_default
    if ( name2 == "b" ):
      value_out = byname.beta
    if ( name2 == "g" or name2 == "*" ):
      byname.gamma = byname.gamma_default
    if ( name2 == "g" ):
      value_out = byname.gamma
  elif ( action2 == "s" ):
    if ( name2 == "a" ):
      byname.alpha = value_in
      value_out = byname.alpha
    if ( name2 == "b" ):
      byname.beta = value_in
      value_out = byname.beta
    if ( name2 == "g" ):
      byname.gamma = value_in
      value_out = byname.gamma

  return value_out

def byname_test ( ):

#*****************************************************************************80
#
## byname_test() tests byname().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'byname_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test byname(), with the interface:' )
  print ( '    value_out = byname(action,name,value_in)' )
  print ( '' )
  print ( '    byname ( "print", "*", None )' )
  byname ( "print", "*", None )
  print ( '    alpha = byname ( "set", "alpha", 1.0 )' )
  alpha = byname ( "set", "alpha", 1.0 )
  print ( '    beta = byname ( "set", "beta", 99 )' )
  beta = byname ( "set", "beta", 99.0 )
  print ( '    byname ( "set", "gamma", alpha + beta )' )
  byname ( "set", "gamma", alpha + beta )
  print ( '    byname ( "print", "*", None )' )
  byname ( "print", "*", None )
  print ( '    gamma = byname ( "get", "gamma", None )' )
  gamma = byname ( "get", "gamma", None )
  print ( '    byname ( "set", "gamma", 2.0*gamma )' )
  byname ( "set", "gamma", 2.0*gamma )
  print ( '    byname ( "print", "gamma", None )' )
  byname ( "print", "gamma", None )
  print ( '    beta = byname ( "set", "beta", "Shazam!" )' )
  beta = byname ( "set", "beta", "Shazam!" )
  print ( '    byname ( "print", "*", None )' )
  byname ( "print", "*", None )
  print ( '    byname ( "reset", None, None )' )
  byname ( "reset", None, None )
  print ( '    byname ( "print", "*" )' )
  byname ( "print", "*" )
#
#  Terminate.
#
  print ( '' )
  print ( 'byname_test():' )
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
#    21 August 2019
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
  byname_test ( )
  timestamp ( )

