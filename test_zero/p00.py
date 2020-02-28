#! /usr/bin/env python
#
def p00_fx ( prob, x ):

#*****************************************************************************80
#
## P00_FX evaluates a function specified by problem number.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the number of the problem.
#
#    Input, real X, the point at which F is to be evaluated.
#
#    Output, real FX, the value of the function at X.
#
  from p01 import p01_fx
  from p02 import p02_fx
  from p03 import p03_fx
  from p04 import p04_fx
  from p05 import p05_fx
  from p06 import p06_fx
  from p07 import p07_fx
  from p08 import p08_fx
  from p09 import p09_fx
  from p10 import p10_fx
  from p11 import p11_fx
  from p12 import p12_fx
  from p13 import p13_fx
  from p14 import p14_fx
  from p15 import p15_fx
  from p16 import p16_fx
  from p17 import p17_fx
  from p18 import p18_fx
  from p19 import p19_fx
  from sys import exit

  if ( prob == 1 ):
    fx = p01_fx ( x )
  elif ( prob == 2 ):
    fx = p02_fx ( x )
  elif ( prob == 3 ):
    fx = p03_fx ( x )
  elif ( prob == 4 ):
    fx = p04_fx ( x )
  elif ( prob == 5 ):
    fx = p05_fx ( x )
  elif ( prob == 6 ):
    fx = p06_fx ( x )
  elif ( prob == 7 ):
    fx = p07_fx ( x )
  elif ( prob == 8 ):
    fx = p08_fx ( x )
  elif ( prob == 9 ):
    fx = p09_fx ( x )
  elif ( prob == 10 ):
    fx = p10_fx ( x )
  elif ( prob == 11 ):
    fx = p11_fx ( x )
  elif ( prob == 12 ):
    fx = p12_fx ( x )
  elif ( prob == 13 ):
    fx = p13_fx ( x )
  elif ( prob == 14 ):
    fx = p14_fx ( x )
  elif ( prob == 15 ):
    fx = p15_fx ( x )
  elif ( prob == 16 ):
    fx = p16_fx ( x )
  elif ( prob == 17 ):
    fx = p17_fx ( x )
  elif ( prob == 18 ):
    fx = p18_fx ( x )
  elif ( prob == 19 ):
    fx = p19_fx ( x )
  else:
    print ( '' )
    print ( 'P00_FX - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    exit ( 'P00_FX - Fatal error!' )

  return fx

def p00_fx1 ( prob, x ):

#*****************************************************************************80
#
## P00_FX1: first derivative of a function specified by problem number.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the number of the problem.
#
#    Input, real X, the point at which F is to be evaluated.
#
#    Output, real FX1, the first derivative of the function at X.
#
  from p01 import p01_fx1
  from p02 import p02_fx1
  from p03 import p03_fx1
  from p04 import p04_fx1
  from p05 import p05_fx1
  from p06 import p06_fx1
  from p07 import p07_fx1
  from p08 import p08_fx1
  from p09 import p09_fx1
  from p10 import p10_fx1
  from p11 import p11_fx1
  from p12 import p12_fx1
  from p13 import p13_fx1
  from p14 import p14_fx1
  from p15 import p15_fx1
  from p16 import p16_fx1
  from p17 import p17_fx1
  from p18 import p18_fx1
  from p19 import p19_fx1
  from sys import exit

  if ( prob == 1 ):
    fx1 = p01_fx1 ( x )
  elif ( prob == 2 ):
    fx1 = p02_fx1 ( x )
  elif ( prob == 3 ):
    fx1 = p03_fx1 ( x )
  elif ( prob == 4 ):
    fx1 = p04_fx1 ( x )
  elif ( prob == 5 ):
    fx1 = p05_fx1 ( x )
  elif ( prob == 6 ):
    fx1 = p06_fx1 ( x )
  elif ( prob == 7 ):
    fx1 = p07_fx1 ( x )
  elif ( prob == 8 ):
    fx1 = p08_fx1 ( x )
  elif ( prob == 9 ):
    fx1 = p09_fx1 ( x )
  elif ( prob == 10 ):
    fx1 = p10_fx1 ( x )
  elif ( prob == 11 ):
    fx1 = p11_fx1 ( x )
  elif ( prob == 12 ):
    fx1 = p12_fx1 ( x )
  elif ( prob == 13 ):
    fx1 = p13_fx1 ( x )
  elif ( prob == 14 ):
    fx1 = p14_fx1 ( x )
  elif ( prob == 15 ):
    fx1 = p15_fx1 ( x )
  elif ( prob == 16 ):
    fx1 = p16_fx1 ( x )
  elif ( prob == 17 ):
    fx1 = p17_fx1 ( x )
  elif ( prob == 18 ):
    fx1 = p18_fx1 ( x )
  elif ( prob == 19 ):
    fx1 = p19_fx1 ( x )
  else:
    print ( '' )
    print ( 'P00_FX1 - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    exit ( 'P00_FX1 - Fatal error!' )

  return fx1

def p00_fx2 ( prob, x ):

#*****************************************************************************80
#
## P00_FX2: second derivative of a function specified by problem number.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the number of the problem.
#
#    Input, real X, the point at which F is to be evaluated.
#
#    Output, real FX2, the second derivative of the function at X.
#
  from p01 import p01_fx2
  from p02 import p02_fx2
  from p03 import p03_fx2
  from p04 import p04_fx2
  from p05 import p05_fx2
  from p06 import p06_fx2
  from p07 import p07_fx2
  from p08 import p08_fx2
  from p09 import p09_fx2
  from p10 import p10_fx2
  from p11 import p11_fx2
  from p12 import p12_fx2
  from p13 import p13_fx2
  from p14 import p14_fx2
  from p15 import p15_fx2
  from p16 import p16_fx2
  from p17 import p17_fx2
  from p18 import p18_fx2
  from p19 import p19_fx2
  from sys import exit

  if ( prob == 1 ):
    fx2 = p01_fx2 ( x )
  elif ( prob == 2 ):
    fx2 = p02_fx2 ( x )
  elif ( prob == 3 ):
    fx2 = p03_fx2 ( x )
  elif ( prob == 4 ):
    fx2 = p04_fx2 ( x )
  elif ( prob == 5 ):
    fx2 = p05_fx2 ( x )
  elif ( prob == 6 ):
    fx2 = p06_fx2 ( x )
  elif ( prob == 7 ):
    fx2 = p07_fx2 ( x )
  elif ( prob == 8 ):
    fx2 = p08_fx2 ( x )
  elif ( prob == 9 ):
    fx2 = p09_fx2 ( x )
  elif ( prob == 10 ):
    fx2 = p10_fx2 ( x )
  elif ( prob == 11 ):
    fx2 = p11_fx2 ( x )
  elif ( prob == 12 ):
    fx2 = p12_fx2 ( x )
  elif ( prob == 13 ):
    fx2 = p13_fx2 ( x )
  elif ( prob == 14 ):
    fx2 = p14_fx2 ( x )
  elif ( prob == 15 ):
    fx2 = p15_fx2 ( x )
  elif ( prob == 16 ):
    fx2 = p16_fx2 ( x )
  elif ( prob == 17 ):
    fx2 = p17_fx2 ( x )
  elif ( prob == 18 ):
    fx2 = p18_fx2 ( x )
  elif ( prob == 19 ):
    fx2 = p19_fx2 ( x )
  else:
    print ( '' )
    print ( 'P00_FX2 - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    exit ( 'P00_FX2 - Fatal error!' )

  return fx2

def p00_prob_num ( ):

#*****************************************************************************80
#
## P00_PROB_NUM returns the number of problems available.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer PROB_NUM, the number of problems available.
#
  prob_num = 19

  return prob_num

def p00_rang ( prob ):

#*****************************************************************************80
#
## P00_RANG returns an interval bounding the root for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the number of the problem.
#
#    Output, real RANG(2), the minimum and maximum values of
#    an interval containing the root.
#
  from p01 import p01_rang
  from p02 import p02_rang
  from p03 import p03_rang
  from p04 import p04_rang
  from p05 import p05_rang
  from p06 import p06_rang
  from p07 import p07_rang
  from p08 import p08_rang
  from p09 import p09_rang
  from p10 import p10_rang
  from p11 import p11_rang
  from p12 import p12_rang
  from p13 import p13_rang
  from p14 import p14_rang
  from p15 import p15_rang
  from p16 import p16_rang
  from p17 import p17_rang
  from p18 import p18_rang
  from p19 import p19_rang
  from sys import exit

  if ( prob == 1 ):
    rang = p01_rang ( )
  elif ( prob == 2 ):
    rang = p02_rang ( )
  elif ( prob == 3 ):
    rang = p03_rang ( )
  elif ( prob == 4 ):
    rang = p04_rang ( )
  elif ( prob == 5 ):
    rang = p05_rang ( )
  elif ( prob == 6 ):
    rang = p06_rang ( )
  elif ( prob == 7 ):
    rang = p07_rang ( )
  elif ( prob == 8 ):
    rang = p08_rang ( )
  elif ( prob == 9 ):
    rang = p09_rang ( )
  elif ( prob == 10 ):
    rang = p10_rang ( )
  elif ( prob == 11 ):
    rang = p11_rang ( )
  elif ( prob == 12 ):
    rang = p12_rang ( )
  elif ( prob == 13 ):
    rang = p13_rang ( )
  elif ( prob == 14 ):
    rang = p14_rang ( )
  elif ( prob == 15 ):
    rang = p15_rang ( )
  elif ( prob == 16 ):
    rang = p16_rang ( )
  elif ( prob == 17 ):
    rang = p17_rang ( )
  elif ( prob == 18 ):
    rang = p18_rang ( )
  elif ( prob == 19 ):
    rang = p19_rang ( )
  else:
    print ( '' )
    print ( 'P00_RANG - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    exit ( 'P00_RANG - Fatal error!' )

  return rang

def p00_root ( prob, i ):

#*****************************************************************************80
#
## P00_ROOT returns a known root for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the number of the problem.
#
#    Input, integer I, the index of the root to return.
#
#    Output, real X, the I-th root.
#
  from p01 import p01_root
  from p02 import p02_root
  from p03 import p03_root
  from p04 import p04_root
  from p05 import p05_root
  from p06 import p06_root
  from p07 import p07_root
  from p08 import p08_root
  from p09 import p09_root
  from p10 import p10_root
  from p11 import p11_root
  from p12 import p12_root
  from p13 import p13_root
  from p14 import p14_root
  from p15 import p15_root
  from p16 import p16_root
  from p17 import p17_root
  from p18 import p18_root
  from p19 import p19_root
  from sys import exit

  if ( prob == 1 ):
    x = p01_root ( i )
  elif ( prob == 2 ):
    x = p02_root ( i )
  elif ( prob == 3 ):
    x = p03_root ( i )
  elif ( prob == 4 ):
    x = p04_root ( i )
  elif ( prob == 5 ):
    x = p05_root ( i )
  elif ( prob == 6 ):
    x = p06_root ( i )
  elif ( prob == 7 ):
    x = p07_root ( i )
  elif ( prob == 8 ):
    x = p08_root ( i )
  elif ( prob == 9 ):
    x = p09_root ( i )
  elif ( prob == 10 ):
    x = p10_root ( i )
  elif ( prob == 11 ):
    x = p11_root ( i )
  elif ( prob == 12 ):
    x = p12_root ( i )
  elif ( prob == 13 ):
    x = p13_root ( i )
  elif ( prob == 14 ):
    x = p14_root ( i )
  elif ( prob == 15 ):
    x = p15_root ( i )
  elif ( prob == 16 ):
    x = p16_root ( i )
  elif ( prob == 17 ):
    x = p17_root ( i )
  elif ( prob == 18 ):
    x = p18_root ( i )
  elif ( prob == 19 ):
    x = p19_root ( i )
  else:
    print ( '' )
    print ( 'P00_ROOT - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    exit ( 'P00_ROOT - Fatal error!' )

  return x

def p00_root_num ( prob ):

#*****************************************************************************80
#
## P00_ROOT_NUM returns the number of known roots for a problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the number of the problem.
#
#    Output, integer ROOT_NUM, the number of known roots.
#    This value may be zero.
#
  from p01 import p01_root_num
  from p02 import p02_root_num
  from p03 import p03_root_num
  from p04 import p04_root_num
  from p05 import p05_root_num
  from p06 import p06_root_num
  from p07 import p07_root_num
  from p08 import p08_root_num
  from p09 import p09_root_num
  from p10 import p10_root_num
  from p11 import p11_root_num
  from p12 import p12_root_num
  from p13 import p13_root_num
  from p14 import p14_root_num
  from p15 import p15_root_num
  from p16 import p16_root_num
  from p17 import p17_root_num
  from p18 import p18_root_num
  from p19 import p19_root_num
  from sys import exit

  if ( prob == 1 ):
    root_num = p01_root_num ( )
  elif ( prob == 2 ):
    root_num = p02_root_num ( )
  elif ( prob == 3 ):
    root_num = p03_root_num ( )
  elif ( prob == 4 ):
    root_num = p04_root_num ( )
  elif ( prob == 5 ):
    root_num = p05_root_num ( )
  elif ( prob == 6 ):
    root_num = p06_root_num ( )
  elif ( prob == 7 ):
    root_num = p07_root_num ( )
  elif ( prob == 8 ):
    root_num = p08_root_num ( )
  elif ( prob == 9 ):
    root_num = p09_root_num ( )
  elif ( prob == 10 ):
    root_num = p10_root_num ( )
  elif ( prob == 11 ):
    root_num = p11_root_num ( )
  elif ( prob == 12 ):
    root_num = p12_root_num ( )
  elif ( prob == 13 ):
    root_num = p13_root_num ( )
  elif ( prob == 14 ):
    root_num = p14_root_num ( )
  elif ( prob == 15 ):
    root_num = p15_root_num ( )
  elif ( prob == 16 ):
    root_num = p16_root_num ( )
  elif ( prob == 17 ):
    root_num = p17_root_num ( )
  elif ( prob == 18 ):
    root_num = p18_root_num ( )
  elif ( prob == 19 ):
    root_num = p19_root_num ( )
  else:
    print ( '' )
    print ( 'P00_ROOT_NUM - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    exit ( 'P00_ROOT_NUM - Fatal error!' )

  return root_num

def p00_start ( prob, i ):

#*****************************************************************************80
#
## P00_START returns a starting point for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the number of the problem.
#
#    Input, integer I, the index of the starting point.
#
#    Output, real X, the starting point.
#
  from p01 import p01_start
  from p02 import p02_start
  from p03 import p03_start
  from p04 import p04_start
  from p05 import p05_start
  from p06 import p06_start
  from p07 import p07_start
  from p08 import p08_start
  from p09 import p09_start
  from p10 import p10_start
  from p11 import p11_start
  from p12 import p12_start
  from p13 import p13_start
  from p14 import p14_start
  from p15 import p15_start
  from p16 import p16_start
  from p17 import p17_start
  from p18 import p18_start
  from p19 import p19_start
  from sys import exit

  if ( prob == 1 ):
    x = p01_start ( i )
  elif ( prob == 2 ):
    x = p02_start ( i )
  elif ( prob == 3 ):
    x = p03_start ( i )
  elif ( prob == 4 ):
    x = p04_start ( i )
  elif ( prob == 5 ):
    x = p05_start ( i )
  elif ( prob == 6 ):
    x = p06_start ( i )
  elif ( prob == 7 ):
    x = p07_start ( i )
  elif ( prob == 8 ):
    x = p08_start ( i )
  elif ( prob == 9 ):
    x = p09_start ( i )
  elif ( prob == 10 ):
    x = p10_start ( i )
  elif ( prob == 11 ):
    x = p11_start ( i )
  elif ( prob == 12 ):
    x = p12_start ( i )
  elif ( prob == 13 ):
    x = p13_start ( i )
  elif ( prob == 14 ):
    x = p14_start ( i )
  elif ( prob == 15 ):
    x = p15_start ( i )
  elif ( prob == 16 ):
    x = p16_start ( i )
  elif ( prob == 17 ):
    x = p17_start ( i )
  elif ( prob == 18 ):
    x = p18_start ( i )
  elif ( prob == 19 ):
    x = p19_start ( i )
  else:
    print ( '' )
    print ( 'P00_START - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    exit ( 'P00_START - Fatal error!' )

  return x

def p00_start_num ( prob ):

#*****************************************************************************80
#
## P00_START_NUM returns the number of starting points for a problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the number of the problem.
#
#    Output, integer START_NUM, the number of starting points.
#
  from p01 import p01_start_num
  from p02 import p02_start_num
  from p03 import p03_start_num
  from p04 import p04_start_num
  from p05 import p05_start_num
  from p06 import p06_start_num
  from p07 import p07_start_num
  from p08 import p08_start_num
  from p09 import p09_start_num
  from p10 import p10_start_num
  from p11 import p11_start_num
  from p12 import p12_start_num
  from p13 import p13_start_num
  from p14 import p14_start_num
  from p15 import p15_start_num
  from p16 import p16_start_num
  from p17 import p17_start_num
  from p18 import p18_start_num
  from p19 import p19_start_num
  from sys import exit

  if ( prob == 1 ):
    start_num = p01_start_num ( )
  elif ( prob == 2 ):
    start_num = p02_start_num ( )
  elif ( prob == 3 ):
    start_num = p03_start_num ( )
  elif ( prob == 4 ):
    start_num = p04_start_num ( )
  elif ( prob == 5 ):
    start_num = p05_start_num ( )
  elif ( prob == 6 ):
    start_num = p06_start_num ( )
  elif ( prob == 7 ):
    start_num = p07_start_num ( )
  elif ( prob == 8 ):
    start_num = p08_start_num ( )
  elif ( prob == 9 ):
    start_num = p09_start_num ( )
  elif ( prob == 10 ):
    start_num = p10_start_num ( )
  elif ( prob == 11 ):
    start_num = p11_start_num ( )
  elif ( prob == 12 ):
    start_num = p12_start_num ( )
  elif ( prob == 13 ):
    start_num = p13_start_num ( )
  elif ( prob == 14 ):
    start_num = p14_start_num ( )
  elif ( prob == 15 ):
    start_num = p15_start_num ( )
  elif ( prob == 16 ):
    start_num = p16_start_num ( )
  elif ( prob == 17 ):
    start_num = p17_start_num ( )
  elif ( prob == 18 ):
    start_num = p18_start_num ( )
  elif ( prob == 19 ):
    start_num = p19_start_num ( )
  else:
    print ( '' )
    print ( 'P00_START_NUM - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    exit ( 'P00_START_NUM - Fatal error!' )

  return start_num

def p00_title ( prob ):

#*****************************************************************************80
#
## P00_TITLE returns the title for a given problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the number of the problem.
#
#    Output, string TITLE, the title of the given problem.
#
  from p01 import p01_title
  from p02 import p02_title
  from p03 import p03_title
  from p04 import p04_title
  from p05 import p05_title
  from p06 import p06_title
  from p07 import p07_title
  from p08 import p08_title
  from p09 import p09_title
  from p10 import p10_title
  from p11 import p11_title
  from p12 import p12_title
  from p13 import p13_title
  from p14 import p14_title
  from p15 import p15_title
  from p16 import p16_title
  from p17 import p17_title
  from p18 import p18_title
  from p19 import p19_title
  from sys import exit

  if ( prob == 1 ):
    title = p01_title ( )
  elif ( prob == 2 ):
    title = p02_title ( )
  elif ( prob == 3 ):
    title = p03_title ( )
  elif ( prob == 4 ):
    title = p04_title ( )
  elif ( prob == 5 ):
    title = p05_title ( )
  elif ( prob == 6 ):
    title = p06_title ( )
  elif ( prob == 7 ):
    title = p07_title ( )
  elif ( prob == 8 ):
    title = p08_title ( )
  elif ( prob == 9 ):
    title = p09_title ( )
  elif ( prob == 10 ):
    title = p10_title ( )
  elif ( prob == 11 ):
    title = p11_title ( )
  elif ( prob == 12 ):
    title = p12_title ( )
  elif ( prob == 13 ):
    title = p13_title ( )
  elif ( prob == 14 ):
    title = p14_title ( )
  elif ( prob == 15 ):
    title = p15_title ( )
  elif ( prob == 16 ):
    title = p16_title ( )
  elif ( prob == 17 ):
    title = p17_title ( )
  elif ( prob == 18 ):
    title = p18_title ( )
  elif ( prob == 19 ):
    title = p19_title ( )
  else:
    print ( '' )
    print ( 'P00_TITLE - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    error ( 'P00_TITLE - Fatal error!' )

  return title

