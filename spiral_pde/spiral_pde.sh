#! /bin/bash
#
echo "Do not run this example.  It takes too long!"
exit
#
python3 spiral_pde.py > spiral_pde.txt
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
