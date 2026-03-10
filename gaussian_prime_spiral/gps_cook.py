#! /usr/bin/env python3
#
from sympy import isprime
import matplotlib.pyplot as plt

def isgaussprime ( z: complex ):
  a, b = int ( z.real ), int ( z.imag )
  if a*b != 0:
    return isprime ( a**2 + b**2 )
  else:
    c = abs ( a + b )
    return isprime ( c ) and c % 4 == 3

def connect ( z1: complex, z2: complex ):
  plt.plot ( [z1.real, z2.real], [z1.imag, z2.imag], 'b' )

def gps_cook ( start = 3 + 5j ):  

# start = 127 + 130j

  step = 1
  z = start
  next = None

  while next != start:
    next = z + step
    connect ( z, next )
    if isgaussprime ( next ):
      step *= 1j
    z = next

  plt.axis ( 'Equal' )
  filename = 'gps_cook.png' )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

if ( __name__ == "__main__" ):
  gps_cook ( 3 + 5j )

