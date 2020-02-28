#! /bin/bash
#
python3 r8ge.py > r8ge.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit
fi
#
#  Get rid of obnoxious garbage.
#
rm -f *.pyc
rm -rf __pycache__
#
echo "Normal end of execution."
