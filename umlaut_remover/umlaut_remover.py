#! /usr/bin/env python3
#
def umlaut_remover ( s1 ):

#*****************************************************************************80
#
## umlaut_remover() adjusts some German special characters by English equivalents.
#
#  Discussion:
#
#    In particular, certain umlauted vowels are replaced by the vowel followed
#    by the letter "e".
#
#    The code also replaces the German double s by "ss".
#
#    The guillemots "<<" and ">>" are replaced by double quotes.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 August 2021
#
#  Author:
#
#    Original Python version by John Berroa,
#    This version by John Burkardt.
#
#  Input:
#
#    string s1: the string of German text.
#
#  Output:
#
#    string s2: the string after substitutions have been made.
#
    oq = '»'.encode()
    cq = '«'.encode()
    u = 'ü'.encode()
    U = 'Ü'.encode()
    a = 'ä'.encode()
    A = 'Ä'.encode()
    o = 'ö'.encode()
    O = 'Ö'.encode()
    ss = 'ß'.encode()

    s2 = s1.encode ( )
    s2 = s2.replace ( u, b'ue' )
    s2 = s2.replace ( U, b'Ue' )
    s2 = s2.replace ( a, b'ae' )
    s2 = s2.replace ( A, b'Ae' )
    s2 = s2.replace ( o, b'oe' )
    s2 = s2.replace ( O, b'Oe' )
    s2 = s2.replace ( ss, b'ss' )
    s2 = s2.replace ( oq, b'"' )
    s2 = s2.replace ( cq, b'"' )

    s2 = s2.decode ( 'utf-8' )

    return s2

def umlaut_remover_string_test ( ):

#*****************************************************************************80
#
## umlaut_remover_string_test() tests umlaut_remover() on a string.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 August 2021
#
#  Author:
#
#    John Burkardt.
#
  print ( "" )
  print ( "umlaut_remover_string_test():" )
  print ( "  umlaut_remover() can modify a string of German text," )
  print ( "  replacing special characters by English equivalents." )

  s1 = "»Dies frühzeitige Aufstehen«, dachte er, »macht einen ganz "\
       "blödsinnig.«  Er fühlte ein leichtes Jucken "\
       "oben auf dem Bauch; schob sich auf dem Rücken langsam "\
       "näher zum Bettpfosten, um den Kopf besser heben "\
       "zu können; fand die juckende Stelle, die mit lauter "\
       "kleinen weißen Pünktchen besetzt war, die er nicht zu "\
       "beurteilen verstand; und wollte mit einem Bein die "\
       "Stelle betasten, zog es aber gleich zurück, denn bei "\
       "der Berührung umwehten ihn Kälteschauer"
  print ( "" )
  print ( "  Initial string:" )
  print ( "" )
  print ( s1 )
  s2 = umlaut_remover ( s1 )
  print ( "" )
  print ( "  Modified string:" )
  print ( "" )
  print ( s2 )

  return

def umlaut_remover_file_test ( ):

#*****************************************************************************80
#
## umlaut_remover_file_test() tests umlaut_remover() on a file.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 August 2021
#
#  Author:
#
#    John Burkardt.
#
  print ( "" )
  print ( "umlaut_remover_file_test():" )
  print ( "  umlaut_remover() can modify a German text file," )
  print ( "  replacing special characters by English equivalents." )

  filename = "die_verwandlung.txt"
  print ( "  Reading '", filename, "'." )
  file = open ( filename, 'r', encoding = 'latin-1' )
  t = file.read ( )
  file.close ( )

  t2 = umlaut_remover ( t )
  filename = "die_verwandlung_normalized.txt"
  print ( "  Writing '", filename, "'." )
  file = open ( filename, 'w' )
  file.write ( t2 )
  file.close ( )

  return

def umlaut_remover_test ( ):

#*****************************************************************************80
#
## umlaut_remover_test() tests umlaut_remover().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 August 2021
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np
  import platform

  print ( "" )
  print ( "umlaut_remover_test:" )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( "  umlaut_remover() replaces some special characters in German text" )
  print ( "  with equivalent English versions." )

  umlaut_remover_string_test ( )
  umlaut_remover_file_test ( )
#
#  Terminate.
#
  print ( "" )
  print ( "umlaut_remover_test():" )
  print ( "  Normal end of execution." )

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
  umlaut_remover_test ( )
  timestamp ( )

