#! /bin/bash
#
python3 navier_stokes_3d_exact.py > navier_stokes_3d_exact.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
#  Get rid of obnoxious garbage.
#
rm -f *.pyc
rm -rf __pycache__
#
echo "Normal end of execution."
