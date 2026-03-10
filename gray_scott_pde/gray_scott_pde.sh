#! /bin/bash
#
echo "Skip execution of gray_scott_pde.  It can take 7 or 8 hours!"
exit
#
python3 gray_scott_pde.py > gray_scott_pde.txt
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
