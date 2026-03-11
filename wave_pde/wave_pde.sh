#! /bin/bash
#
python3 wave_pde.py > wave_pde.txt
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
convert -delay 10 -loop 1 wave_pde*.png wave_pde.gif
#
rm wave_pde_*.png
#
echo "Normal end of execution."
