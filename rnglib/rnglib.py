#! /usr/bin/env python3
#
a_save = [ \
  False, False, False, False, False, False, False, False, \
  False, False, False, False, False, False, False, False, \
  False, False, False, False, False, False, False, False, \
  False, False, False, False, False, False, False, False ];

cg1_save = [ \
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]
cg2_save = [ \
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]

g_save = 1

ig1_save = [ \
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]
ig2_save = [ \
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]

initialized_save = False

lg1_save = [ \
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]
lg2_save = [ \
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]

def advance_state ( k ):

#*****************************************************************************80
#
## advance_state() advances the state of the current generator.
#
#  Discussion:
#
#    This procedure advances the state of the current generator by 2^K
#    values and resets the initial seed to that value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    This version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
#  Input:
#
#    integer K, indicates that the generator is to be
#    advanced by 2^K values.
#    0 <= K.
#
  a1 = 40014
  a2 = 40692
  m1 = 2147483563
  m2 = 2147483399

  if ( k < 0 ):
    print ( '' )
    print ( 'advance_state(): Fatal error!' )
    print ( '  Input exponent K is out of bounds.' )
    raise Exception ( 'advance_state(): Fatal error!' )
#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ( '' )
    print ( 'advance_state(): Note:' )
    print ( '  Initializing rnglib package.' )
    initialize ( )
#
#  Get the current generator index.
#
  g = cgn_get ( )

  b1 = a1
  b2 = a2

  for i in range ( 1, k + 1 ):
    b1 = multmod ( b1, b1, m1 )
    b2 = multmod ( b2, b2, m2 )

  [ cg1, cg2 ] = cg_get ( g )
  cg1 = multmod ( b1, cg1, m1 )
  cg2 = multmod ( b2, cg2, m2 )
  cg_set ( g, cg1, cg2 )

  return

def antithetic_get ( ):

#*****************************************************************************80
#
## antithetic_get() queries the antithetic value for a given generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    bool VALUE, is TRUE if generator G is antithetic.
#
  i = -1
  value = []
  value = antithetic_memory ( i, value )

  return value

def antithetic_memory ( i, value ):

#*****************************************************************************80
#
## antithetic_memory() stores the antithetic value for all generators.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the desired action.
#    -1, get a value.
#    0, initialize all values.
#    1, set a value.
#
#    bool VALUE.  For I = +1, VALUE is an input quantity.
#
#  Output:
#
#    bool VALUE.  For I = -1, VALUE is an output quantity.
#
  global a_save

  g_max = 32

  if ( i < 0 ):
    g = cgn_get ( )
    value = a_save[g-1]
  elif ( i == 0 ):
    a_save = [];
    for i in range ( 1, g_max + 1 ):
      a_save.append ( False )
    value = false
  elif ( 0 < i ):
    g = cgn_get ( )
    a_save[g-1] = value

  return value

def antithetic_set ( value ):

#*****************************************************************************80
#
## antithetic_set() sets the antithetic value for a given generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    bool VALUE, is TRUE if the current generator is to be antithetic.
#
  i = +1
  value = antithetic_memory ( i, value )

  return

def cg_get ( g ):

#*****************************************************************************80
#
## cg_get() queries the CG values for a given generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer G, the index of the generator.
#    1 <= G <= 32.
#
#  Output:
#
#    integer CG1, CG2, the CG values for generator G.
#
  i = -1
  cg1 = []
  cg2 = []
  cg1, cg2 = cg_memory ( i, g, cg1, cg2 )

  return cg1, cg2

def cg_memory ( i, g, cg1, cg2 ):

#*****************************************************************************80
#
## cg_memory() stores the CG values for all generators.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the desired action.
#    -1, get a value.
#    0, initialize all values.
#    1, set a value.
#
#    integer G, for I = -1 or +1, the index of
#    the generator, with 1 <= G <= 32.
#
#    integer CG1, CG2.  For I = +1, these are 
#    new values of the CG parameter for generator G.
#
#  Output:
#
#    integer CG1, CG2.  For I = -1, these are 
#    old values of the CG parameter for generator G.
#
  global cg1_save
  global cg2_save

  g_max = 32

  if ( g < 1 or g_max < g ):
    print ( '' )
    print ( 'cg_memory(): Fatal error!' )
    print ( '  Input generator index G is out of bounds.' )
    raise Exception ( 'cg_memory(): Fatal error!' )

  if ( i < 0 ):
    cg1 = cg1_save[g-1]
    cg2 = cg2_save[g-1]
  elif ( i == 0 ):
    for i in range ( 1, g_max + 1 ):
      cg1_save[i-1] = 0
      cg2_save[i-1] = 0
    cg1 = 0
    cg2 = 0
  elif ( 0 < i ):
    cg1_save[g-1] = cg1
    cg2_save[g-1] = cg2

  return cg1, cg2

def cgn_get ( ):

#*****************************************************************************80
#
## cgn_get() gets the current generator index.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer G, the current generator index.
#
  i = -1
  g = []
  g = cgn_memory ( i, g )

  return g

def cgn_memory ( i, g ):

#*****************************************************************************80
#
## cgn_memory() stores the current generator index.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the desired action.
#    -1, get the value.
#    0, initialize the value.
#    1, set the value.
#
#    integer G.  For I = +1, an input quantity.
#
#  Output:
#
#    integer G.  For I = -1 or 0, an output quantity.
#
  global g_save

  g_max = 32

  if ( i < 0 ):

    g = g_save

  elif ( i == 0 ):

    g_save = 1
    g = g_save

  elif ( 0 < i ):

    if ( g < 1 or g_max < g ):
      print ( '' )
      print ( 'cgn_memory(): Fatal error!' )
      print ( '  Input generator index G is out of bounds.' )
      raise Exception ( 'cgn_memory(): Fatal error!' )

    g_save = g

  return g

def cgn_set ( g ):

#*****************************************************************************80
#
## cgn_set() sets the current generator index.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer G, the current generator index.
#    1 <= G <= 32.
#
  i = +1
  g = cgn_memory ( i, g )

  return

def cg_set ( g, cg1, cg2 ):

#*****************************************************************************80
#
## cg_set() sets the CG values for a given generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer G, the index of the generator.
#    1 <= G <= 32.
#
#    integer CG1, CG2, the CG values for generator G.
#
  i = +1
  cg1, cg2 = cg_memory ( i, g, cg1, cg2 )

  return

def get_state ( ):

#*****************************************************************************80
#
## get_state() returns the state of the current generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    This version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
#  Output:
#
#    integer CG1, CG2, the CG values for the current generator.
#

#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ( '' )
    print ( 'get_state():' )
    print ( '  Initializing rnglib().' )
    initialize ( )
#
#  Get the current generator index.
#
  g = cgn_get ( )
#
#  Retrieve the seed values for this generator.
#
  [ cg1, cg2 ] = cg_get ( g )

  return cg1, cg2

def i4_uni ( ):

#*****************************************************************************80
#
## i4_uni() generates a random positive integer.
#
#  Discussion:
#
#    This procedure returns a random integer following a uniform distribution
#    over (1, 2147483562) using the current generator.
#
#    The original name of this function was "random()", but this conflicts
#    with a standard library function name in C.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    This version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
#  Output:
#
#    integer VALUE, the random integer.
#
  a1 = 40014
  a2 = 40692
  m1 = 2147483563
  m2 = 2147483399
#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ( '' )
    print ( 'i4_uni():' )
    print ( '  Initializing rnglib().' )
    initialize ( )
#
#  Get the current generator index.
#
  g = cgn_get ( )
#
#  Retrieve the seeds for the current generator.
#
  cg1, cg2 = cg_get ( g )
#
#  Update the seeds.
#
  k = ( cg1 // 53668 )
  cg1 = a1 * ( cg1 - k * 53668 ) - k * 12211

  if ( cg1 < 0 ):
    cg1 = cg1 + m1

  k = ( cg2 // 52774 )
  cg2 = a2 * ( cg2 - k * 52774 ) - k * 3791

  if ( cg2 < 0 ):
    cg2 = cg2 + m2
#
#  Store the updated seeds.
#
  cg_set ( g, cg1, cg2 )
#
#  Construct the random integer from the seeds.
#
  z = cg1 - cg2

  if ( z < 1 ):
    z = z + m1 - 1
#
#  If the generator is in antithetic mode, we must reflect the value.
#
  value = antithetic_get ( )

  if ( value ):
    z = m1 - z

  return z

def i4_uni_test ( ):

#*****************************************************************************80
#
## i4_uni_test() tests i4_uni.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_uni_test():' )
  print ( '  i4_uni() returns a random positive integer.' )
  print ( '' )

  for i in range ( 1, 21 ):
    value = i4_uni ( )
    print ( '  %d' % ( value ) )

  return

def ig_get ( g ):

#*****************************************************************************80
#
## ig_get() queries the IG values for a given generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer G, the index of the generator.
#    1 <= G <= 32.
#
#  Output:
#
#    integer IG1, IG2, the IG values for generator G.
#
  i = -1
  ig1 = []
  ig2 = []
  ig1, ig2 = ig_memory ( i, g, ig1, ig2 )

  return ig1, ig2

def ig_memory ( i, g, ig1, ig2 ):

#*****************************************************************************80
#
## ig_memory() stores the IG values for all generators.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the desired action.
#    -1, get a value.
#    0, initialize all values.
#    1, set a value.
#
#    integer G, for I = -1 or +1, the index of
#    the generator, with 1 <= G <= 32.
#
#    integer IG1, IG2.  For I = +1, these are 
#    new values of the IG parameter for generator G.
#
#  Output:
#
#    integer IG1, IG2.  For I = -1, these are 
#    old values of the IG parameter for generator G.
#
  global ig1_save
  global ig2_save

  g_max = 32

  if ( g < 1 or g_max < g ):
    print ( '' )
    print ( 'ig_memory(): Fatal error!' )
    print ( '  Input generator index G is out of bounds.' )
    raise Exception ( 'ig_memory(): Fatal error!' )

  if ( i < 0 ):
    ig1 = ig1_save[g-1]
    ig2 = ig2_save[g-1]
  elif ( i == 0 ):
    for j in range ( 1, g_max + 1 ):
      ig1_save[j-1] = 0
      ig2_save[j-1] = 0
    ig1 = 0
    ig2 = 0
  elif ( 0 < i ):
    ig1_save[g-1] = ig1
    ig2_save[g-1] = ig2

  return ig1, ig2

def ig_set ( g, ig1, ig2 ):

#*****************************************************************************80
#
## ig_set() sets the IG values for a given generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer G, the index of the generator.
#    1 <= G <= 32.
#
#    integer IG1, IG2, the IG values for generator G.
#
  i = +1
  ig1, ig2 = ig_memory ( i, g, ig1, ig2 )

  return

def init_generator ( t ):

#*****************************************************************************80
#
## init_generator() sets the current generator to initial, last or new seed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    This version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
#  Input:
#
#    integer T, the seed type:
#    0, use the seed chosen at initialization time.
#    1, use the last seed.
#    2, use a new seed set 2^30 values away.
#
  a1_w = 1033780774
  a2_w = 1494757890
  m1 = 2147483563
  m2 = 2147483399
#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ( '' )
    print ( 'init_generator():' )
    print ( '  Initializing rnglib package.' )
    initialize ( )
#
#  Get the current generator index.
#
  g = cgn_get ( )
#
#  0: Restore the initial seed.
#
  if ( t == 0 ):

    ig1, ig2 = ig_get ( g )
    lg1 = ig1
    lg2 = ig2
    lg_set ( g, lg1, lg2 )
#
#  1: Restore the last seed.
#
  elif ( t == 1 ):

    lg1, lg2 = lg_get ( g );
#
#  Advance to a new seed.
#
  elif ( t == 2 ):

    lg1, lg2 = lg_get ( g )
    lg1 = multmod ( a1_w, lg1, m1 )
    lg2 = multmod ( a2_w, lg2, m2 )
    lg_set ( g, lg1, lg2 )

  else:

    print ( '' )
    print ( 'init_generator(): Fatal error!' )
    print ( '  Input parameter T out of bounds.' )
    raise Exception ( 'init_generator(): Fatal error!' )
#
#  Store the new seed.
#
  cg1 = lg1
  cg2 = lg2
  cg_set ( g, cg1, cg2 )

  return

def initialized_get ( ):

#*****************************************************************************80
#
## initialized_get() gets the initialized value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    bool initialized, is true if the package has been initialized.
#
  i = -1
  initialized = []
  initialized = initialized_memory ( i, initialized )

  return initialized

def initialized_memory ( i, initialized ):

#*****************************************************************************80
#
## initialized_memory() stores the initialized value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the desired action.
#    -1, get a value.
#    0, initialize all values.
#    1, set a value.
#
#    bool initialized.  For I = +1, an input quantity.
#
#  Output:
#
#    bool initialized.  For I = -1, an output quantity.
#
  global initialized_save

  if ( i < 0 ):
    initialized = initialized_save
  elif ( i == 0 ):
    initialized_save = False
    initialized = False
  elif ( 0 < i ):
    initialized_save = initialized

  return initialized

def initialized_set ( ):

#*****************************************************************************80
#
## initialized_set() sets the initialized value to true.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
  i = +1
  initialized = True
  initialized = initialized_memory ( i, initialized )

  return

def initialize ( ):

#*****************************************************************************80
#
## initialize() initializes the random number generator library.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    This version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
  g_max = 32
#
#  Remember that we have called initialize().
#
  initialized_set ( )
#
#  initialize all generators to have FALSE antithetic value.
#
  value = False
  for g in range ( 1, g_max + 1 ):
    cgn_set ( g )
    antithetic_set ( value )
#
#  Set the initial seeds.
#
  ig1 = 1234567890
  ig2 = 123456789
  set_initial_seed ( ig1, ig2 )
#
#  initialize the current generator index to 1.
#
  g = 1
  cgn_set ( g )

  print ( '' )
  print ( 'initialize():' )
  print ( '  rnglib() has been initialized.' )
  return

def lg_get ( g ):

#*****************************************************************************80
#
## lg_get() queries the LG values for a given generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer G, the index of the generator.
#    1 <= G <= 32.
#
#  Output:
#
#    integer LG1, LG2, the LG values for generator G.
#
  i = -1
  lg1 = []
  lg2 = []
  lg1, lg2 = lg_memory ( i, g, lg1, lg2 )

  return lg1, lg2

def lg_memory ( i, g, lg1, lg2 ):

#*****************************************************************************80
#
## lg_memory() stores the LG values for all generators.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the desired action.
#    -1, get a value.
#    0, initialize all values.
#    1, set a value.
#
#    integer G, for I = -1 or +1, the index of
#    the generator, with 1 <= G <= 32.
#
#    integer LG1, LG2.  For I = +1, these are 
#    new values of the LG parameter for generator G.
#
#  Output:
#
#    integer LG1, LG2.  For I = -1, these are 
#    old values of the LG parameter for generator G.
#
  global lg1_save
  global lg2_save

  g_max = 32

  if ( g < 1 or g_max < g ):
    print ( '' )
    print ( 'lg_memory(): Fatal error!' )
    print ( '  Input generator index G is out of bounds.' )
    raise Exception ( 'lg_memory(): Fatal error!' )

  if ( i < 0 ):
    lg1 = lg1_save[g-1]
    lg2 = lg2_save[g-1]
  elif ( i == 0 ):
    for j in range ( 1, g_max + 1 ):
      lg1_save[j-1] = 0
      lg2_save[j-1] = 0
    lg1 = 0
    lg2 = 0
  elif ( 0 < i ):
    lg1_save[g-1] = lg1
    lg2_save[g-1] = lg2

  return lg1, lg2

def lg_set ( g, lg1, lg2 ):

#*****************************************************************************80
#
## lg_set() sets the LG values for a given generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer G, the index of the generator.
#    1 <= G <= 32.
#
#    integer LG1, LG2, the LG values for generator G.
#
  i = +1
  lg_memory ( i, g, lg1, lg2 )

  return

def multmod ( a, s, m ):

#*****************************************************************************80
#
## multmod() carries out modular multiplication.
#
#  Discussion:
#
#    This procedure returns
#
#      ( A * S ) mod M
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    This version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
#  Input:
#
#    integer A, S, M, the arguments.
#
#  Output:
#
#    integer VALUE, the value of the product of A and S,
#    modulo M.
#
  h = 32768

  if ( a <= 0 ):
    print ( '' )
    print ( 'multmod(): Fatal error!' )
    print ( '  A <= 0.' )
    raise Exception ( 'multmod(): Fatal error!' )

  if ( m <= a ):
    print ( '' )
    print ( 'multmod(): Fatal error!' )
    print ( '  M <= A.' )
    raise Exception ( 'multmod(): Fatal error!' )

  if ( s <= 0 ):
    print ( '' )
    print ( 'multmod(): Fatal error!' )
    print ( '  S <= 0.' )
    raise Exception ( 'multmod(): Fatal error!' )

  if ( m <= s ):
    print ( '' )
    print ( 'multmod(): Fatal error!' )
    print ( '  M <= S.' )
    raise Exception ( 'multmod(): Fatal error!' )

  if ( a < h ):

    a0 = a
    p = 0

  else:

    a1 = ( a // h )
    a0 = a - h * a1
    qh = ( m // h )
    rh = m - h * qh

    if ( h <= a1 ):

      a1 = a1 - h
      k = ( s // qh )
      p = h * ( s - k * qh ) - k * rh

      while ( p < 0 ):
        p = p + m

    else:

      p = 0

    if ( a1 != 0 ):

      q = ( m // a1 )
      k = ( s // q )
      p = p - k * ( m - a1 * q )

      if ( 0 < p ):
        p = p - m

      p = p + a1 * ( s - k * q )

      while ( p < 0 ):
        p = p + m

    k = ( p // qh )
    p = h * ( p - k * qh ) - k * rh

    while ( p < 0 ):
      p = p + m

  if ( a0 != 0 ):

    q = ( m // a0 )
    k = ( s // q )
    p = p - k * ( m - a0 * q )

    if ( 0 < p ):
      p = p - m

    p = p + a0 * ( s - k * q )

    while ( p < 0 ):
      p = p + m

  return p

def r4_uni_01 ( ):

#*****************************************************************************80
#
## r4_uni_01() returns a uniform random real number in [0,1].
#
#  Discussion:
#
#    This procedure returns a random floating point number from a uniform
#    distribution over (0,1), not including the endpoint values, using the
#    current random number generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    This version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
#  Output:
#
#    real VALUE, a uniform random value in [0,1].
#
 
#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ( '' )
    print ( 'r4_uniform_01(): Note:' )
    print ( '  Initializing rnglib().' )
    initialize ( )
#
#  Get a random positive integer.
#
  i = i4_uni ( )
#
#  Scale it to a random real in [0,1].
#
  value = i * 4.656613057E-10

  return value

def r4_uni_01_test ( ):

#*****************************************************************************80
#
## r4_uni_01_test() tests r4_uni_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r4_uni_01_test():' )
  print ( '  r4_uni_01() produces a sequence of random values.' )

  print ( '' )
  print ( '  r4_uni_01()' )
  print ( '' )
  for i in range ( 0, 10 ):
    x = r4_uni_01 ()
    print ( '  %g' % ( x ) )

  return

def r8_uni_01 ( ):

#*****************************************************************************80
#
## r8_uni_01() returns a uniform random real number in [0,1].
#
#  Discussion:
#
#    This procedure returns a random floating point number from a uniform
#    distribution over (0,1), not including the endpoint values, using the
#    current random number generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    This version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
#  Output:
#
#    real VALUE, a uniform random value in [0,1].
#

#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ( '' )
    print ( 'r8_uni_01():' )
    print ( '  Initializing rnglib().' )
    initialize ( )
#
#  Get a random positive integer.
#
  i = i4_uni ( )
#
#  Scale it to a random real in [0,1].
#
  value = i * 4.656613057E-10

  return value

def r8_uni_01_test ( ):

#*****************************************************************************80
#
## r8_uni_01_test() tests r8_uni_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_uni_01_test():' )
  print ( '  r8_uni_01() produces a sequence of random values.' )

  print ( '' )
  print ( '  r8_uni_01()' )
  print ( '' )
  for i in range ( 0, 10 ):
    x = r8_uni_01 ()
    print ( '  %g' % ( x ) )

  return

def rnglib_test ( ):

#*****************************************************************************80
#
## rnglib_test() tests rnglib().
#
#  Discussion:
#
#    rnglib_test calls sample problems for the rnglib library.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'rnglib_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test rnglib().' )
#
#  initialize 
#
  initialize ( )
#
#  Call tests.
#
  i4_uni_test ( )
  r8_uni_01_test ( )

  rnglib_test03 ( )
  rnglib_test04 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'rnglib_test():' )
  print ( '  Normal end of execution.' )

  return

def rnglib_test03 ( ):

#*****************************************************************************80
#
## rnglib_test03() demonstrates how the seed can be reset to its initial or last value.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'rnglib_test03():' )
  print ( '  r4_uni_01() returns a random real number' )
  print ( '  in [0,1] using the current generator.' )
#
#  initialize the package.
#
  print ( '' )
  print ( '  initialize() initializes the random number generator.' )
  print ( '  It only needs to be called once before using the package.' )

  initialize ( )

  print ( '' )
  print ( '  init_generator() can reset the seed to the initial value,' )
  print ( '  the last (previous) value, or a new seed.' )
#
#  Set the current generator index to 17.
#
  g = 17
  cgn_set ( g )
  print ( '' )
  print ( '  Current generator index = %d' % ( g ) )
#
#  Force the current generator to begin at its initial seed.
#
  print ( '' )
  print ( '  init_generator(0) starts at the initial seed.' )

  init_generator ( 0 )

  print ( '' )
  print ( '   I    r4_uni_01 ( )' )
  print ( '' )
  for i in range ( 1, 10 ):
    u = r4_uni_01 ( )
    print ( '  %2d  %14.6g' % ( i, u ) )

  print ( '' )
  print ( '  Calling init_generator(0) again restarts' )
  print ( '  at the initial seed.' )

  init_generator ( 0 )

  print ( '' )
  print ( '   I    r4_uni_01 ( )' )
  print ( '' )
  for i in range ( 1, 10 ):
    u = r4_uni_01 ( )
    print ( '  %2d  %14.6g' % ( i, u ) )

  print ( '' )
  print ( '  Calling init_generator ( 2 ) restarts' )
  print ( '  at a new "far ahead" seed.' )

  init_generator ( 2 )

  print ( '' )
  print ( '   I    r4_uni_01 ( )' )
  print ( '' )
  for i in range ( 1, 10 ):
    u = r4_uni_01 ( )
    print ( '  %2d  %14.6g' % ( i, u ) )

  print ( '' )
  print ( '  Calling init_generator ( 1 ) restarts' )
  print ( '  at the last seed (in this case, the "far ahead"' )
  print ( '  seed specified on the previous call.)' )

  print ( '' )
  print ( '   I    r4_uni_01 ( )' )
  print ( '' )
  for i in range ( 1, 11 ):
    u = r4_uni_01 ( )
    print ( '  %2d  %14.6g' % ( i, u ) )
    if ( ( i % 3 ) == 0 ):
      init_generator ( 1 )
      print ( '  (Reset to last seed)' )

  return

def rnglib_test04 ( ):

#*****************************************************************************80
#
## rnglib_test04() demonstrates the use of multiple streams.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'rnglib_test04():' )
  print ( '  r4_uni_01 ( ) returns a random real number' )
  print ( '  in [0,1] using the current generator.' )
#
#  initialize the package.
#
  print ( '' )
  print ( '  initialize() initializes the random number generator.' )
  print ( '  It only needs to be called once before using the package.' )

  initialize ( )

  print ( '' )
  print ( '  Let us call generators #3, #6 and #9.' )
#
#  Use three separate generators, 3, 6 and 9.
#  Force them to start at their initial seeds.
#
  g = [ 3, 6, 9 ]
  print ( '' )
  for j in range ( 0, 3 ):
    print ( '  initialize generator %d' % ( g[j] ) )
    cgn_set ( g[j] )
    init_generator ( 0 )
#
#  Call the generators in the order 3, 6, 9.
#
  print ( '' )
  print ( '   I    r4_uni_01 ( 3 )  r4_uni_01 ( 6 )  r4_uni_01 ( 9 )' )
  print ( '' )
  for i in range ( 1, 11 ):
    print ( '  %2d' % ( i ) ),
    for j in range ( 0, 3 ):
      cgn_set ( g[j] )
      u = r4_uni_01 ( )
      print ( '  %14.6g' % ( u ) ),
    print ( '' )
#
#  Restart the generators at their initial seeds.
#
  g = [ 6, 9, 3 ]
  print ( '' )
  for j in range ( 0, 3 ):
    print ( '  Reinitialize generator %d' % ( g[j] ) )
    cgn_set ( g[j] )
    init_generator ( 0 )
#
#  Call them in a different order, same result.
#
  print ( '' )
  print ( '   I    r4_uni_01 ( 6 )  r4_uni_01 ( 9 )  r4_uni_01 ( 3 )' )
  print ( '' )
  for i in range ( 1, 11 ):
    print ( '  %2d' % ( i ) ),
    for j in range ( 0, 3 ):
      cgn_set ( g[j] )
      u = r4_uni_01 ( )
      print ( '  %14.6g' % ( u ) ),
    print ( '' )

  return

def set_initial_seed ( ig1, ig2 ):

#*****************************************************************************80
#
## set_initial_seed() resets the initial seed and state for all generators.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    This version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
#  Input:
#
#    integer IG1, IG2, the initial seed values
#    for the first generator.
#    1 <= IG1 < 2147483563
#    1 <= IG2 < 2147483399
#
  a1_vw = 2082007225
  a2_vw = 784306273
  g_max = 32
  m1 = 2147483563
  m2 = 2147483399

  if ( ig1 < 1 or m1 <= ig1 ):
    print ( '' )
    print ( 'set_initial_seed(): Fatal error!' )
    print ( '  Input parameter IG1 out of bounds.' )
    raise Exception ( 'set_initial_seed(): Fatal error!' )

  if ( ig2 < 1 or m2 <= ig2 ):
    print ( '' )
    print ( 'set_initial_seed(): Fatal error!' )
    print ( '  Input parameter IG2 out of bounds.' )
    raise Exception ( 'set_initial_seed(): Fatal error!' )
#
#  Because initialize calls set_initial_seed, it's not easy to correct
#  the error that arises if set_initial_seed is called before initialize.
#  So don't bother trying.
#
  if ( not initialized_get ( ) ):
    print ( '' )
    print ( 'set_initial_seed(): Fatal error!' )
    print ( '  rnglib() has not been initialized.' )
    raise Exception ( 'set_initial_seed(): Fatal error!' )
#
#  Set the initial seed, then initialize the first generator.
#
  g = 1
  cgn_set ( g )

  ig_set ( g, ig1, ig2 )

  t = 0
  init_generator ( t )
#
#  Now do similar operations for the other generators.
#
  for g in range ( 2, g_max + 1 ):
    cgn_set ( g )
    ig1 = multmod ( a1_vw, ig1, m1 )
    ig2 = multmod ( a2_vw, ig2, m2 )
    ig_set ( g, ig1, ig2 )
    init_generator ( t )
#
#  Now choose the first generator.
#
  g = 1
  cgn_set ( g )

  return

def set_seed ( cg1, cg2 ):

#*****************************************************************************80
#
## set_seed() resets the initial seed and state of the current generator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    This version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
#  Input:
#
#    integer CG1, CG2, the CG values for generator G.
#    1 <= CG1 < 2147483563
#    1 <= CG2 < 2147483399
#
  m1 = 2147483563
  m2 = 2147483399

  if ( cg1 < 1 or m1 <= cg1 ):
    print ( '' )
    print ( 'set_seed(): Fatal error!' )
    print ( '  Input parameter CG1 out of bounds.' )
    raise Exception ( 'set_seed(): Fatal error!' )

  if ( cg2 < 1 or m2 <= cg2 ):
    print ( '' )
    print ( 'set_seed(): Fatal error!' )
    print ( '  Input parameter CG2 out of bounds.' )
    raise Exception ( 'set_seed(): Fatal error!' )
#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ( '' )
    print ( 'set_seed - Note:' )
    print ( '  Initializing rnglib package.' )
    initialize ( )
#
#  Retrieve the current generator index.
#
  g = cgn_get ( )
#
#  Set the seeds.
#
  cg_set ( g, cg1, cg2 )
#
#  initialize the generator.
#
  t = 0
  init_generator ( t )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  rnglib_test ( )
  timestamp ( )

