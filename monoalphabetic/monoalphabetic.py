#! /usr/bin/env python3
#
def monoalphabetic_test ( ):

#*****************************************************************************80
#
## monoalphabetic_test() tests monoalphabetic().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'monoalphabetic_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test monoalphabetic()' )
  print ( '' )
  print ( '  mono_encrypt() encrypts a plain text using a monoalphabetic' )
  print ( '  substitution cipher.' )
  print ( '  mono_decrypt() decrypts an encryted text.' )
#
#  Typewriter code.
#
  print ( '' )
  print ( '  Here we use a "typewriter code" to encrypt the message.' )
  print ( '' )

  abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  code ='QWERTYUIOPASDFGHJKLZXCVBNM'
  plain = 'A man, a plan, a canal - Panama!'
  crypt = mono_encrypt ( code, plain )
  decrypt = mono_decrypt ( code, crypt )
  print ( '' )
  print ( 'ABC:  "' + abc + '"' )
  print ( 'CODE: "' + code + '"' )
  print ( '' )
  print ( 'PLAIN:   "' + plain + '"' )
  print ( 'CRYPT:   "' + crypt + '"' )
  print ( 'DECRYPT: "' + decrypt + '"' )
#
#  All symbol code.
#
  print ( '' )
  print ( '  We can use symbols in the code, but if the plaintext' )
  print ( '  and code both use punctuation, we will have some mistakes.' )
  print ( '' )

  abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  code ='~`!@#$#^&*()-_=+[{]}:,<.>'
  plain = 'A man, a plan, a canal - Panama!'
  crypt = mono_encrypt ( code, plain )
  decrypt = mono_decrypt ( code, crypt )
  print ( '' )
  print ( 'ABC:  "' + abc + '"' )
  print ( 'CODE: "' + code + '"' )
  print ( '' )
  print ( 'PLAIN:   "' + plain + '"' )
  print ( 'CRYPT:   "' + crypt + '"' )
  print ( 'DECRYPT: "' + decrypt + '"' )
#
#  Symmetric (backwards alphabet) code.
#
  print ( '' )
  print ( '  If we use a "symmetric" code, then encrypting twice' )
  print ( '  actually decodes the message.' )
  print ( '' )

  abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  code ='ZYXWVUTSRQPONMLKJIHGFEDCBA'
  plain = 'A man, a plan, a canal - Panama!'
  crypt = mono_encrypt ( code, plain )
  crypt2 = mono_encrypt ( code, crypt )
  print ( '' )
  print ( 'ABC:  "' + abc + '"' )
  print ( 'CODE: "' + code + '"' )
  print ( '' )
  print ( 'PLAIN:   "' + plain + '"' )
  print ( 'CRYPT:   "' + crypt + '"' )
  print ( 'CRYPT2:  "' + crypt2 + '"' )
#
#  Symmetric (backwards alphabet) code.
#
  print ( '' )
  print ( '  Another ATBASH example.' )
  print ( '' )

  abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  code ='ZYXWVUTSRQPONMLKJIHGFEDCBA'
  plain = 'There are a thousand hacking at the branches of evil for every one who is striking at its root.'
  crypt = mono_encrypt ( code, plain )
  crypt2 = mono_encrypt ( code, crypt )
  print ( '' )
  print ( 'ABC:  "' + abc + '"' )
  print ( 'CODE: "' + code + '"' )
  print ( '' )
  print ( 'PLAIN:   "' + plain + '"' )
  print ( 'CRYPT:   "' + crypt + '"' )
  print ( 'CRYPT2:  "' + crypt2 + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'monoalphabetic_test(:' )
  print ( '  Normal end of execution.' )

  return

def mono_decrypt ( code, crypt ):

#*****************************************************************************80
#
## mono_decrypt() decrypts a string using a monoalphabetic substitution code.
#
#  Discussion:
#
#    Only the alphabetic characters A-Z will be encrypted.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string CODE(26), lists the substitutes for 'A' through 'Z'.
#
#    string CRYPT(*), the encrypted version of the string.
#
#  Output:
#
#    string DECRYPTED(*), the decrypted string.
#
  abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#  Characters that don't match are left alone.
#
  decrypted = []
#
#  Each encrypted character that matches symbol J in the code
#  should be replaced by the alphabetic character J.
#
  for c in crypt:
    try:
      index = code.index ( c )
      decrypted.append ( abc[index] )
    except ValueError:
      decrypted.append ( c )
    
  s = ''.join ( decrypted )

  return s

def mono_encrypt ( code, plain ):

#*****************************************************************************80
#
## mono_encrypt() encrypts a string using a monoalphabetic substitution code.
#
#  Discussion:
#
#    Before the string is encrypted, it is converted to uppercase.
#
#    Only the alphabetic characters A-Z will be encrypted.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string CODE(26), lists the substitutes for 'A' through 'Z'.
#
#    string PLAIN(*), the string to be encrypted.
#
#  Output:
#
#    string CRYPT(*), the encrypted version of the string.
#
  abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  crypt = []

  for c in plain:
    try:
      index = abc.index ( c.upper( ) )
      crypt.append ( code[index] )
    except ValueError:
      crypt.append ( c )
      
  s = ''.join ( crypt )

  return s

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
  monoalphabetic_test ( )
  timestamp ( )

