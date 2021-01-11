---
title: NOTE for Transform
---

## Sine Transform

implements the "slow" Fourier transform, intended as a teaching tool and comparison with the fast Fourier transform.

## Cosine Transform

demonstrates some simple properties of the discrete cosine transform (DCT) for real data.
The code is not optimized in any way, and is intended instead for investigation and education.

## Polyomino Transfrom

transforms the matrix representing a polyomino by reflection and rotation.
The polyomino is described by an MxN matrix containing only 0 and 1 values.
A reflection is implemented by reversing the order of entries in each row.
A rotation of 90 degrees rotates the matrix counterclockwise.
The values of M and N are also interchanged.
The transformation to be carried out will involve 0 or 1 reflections, followed by 0, 1, 2 or 3 rotations of 90 degrees.
