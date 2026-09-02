#! /bin/bash
#
python3 lbm.py > lbm.txt
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
convert -delay 100 -loop 0 ./lbm_output/*.png lbm.gif
if [ $? -ne 0 ]; then
  echo "Animation error."
  exit 1
fi
#
rm -r lbm_output
#
echo "Normal end of execution."
