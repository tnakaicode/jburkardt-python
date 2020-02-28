#! /bin/bash
#
python3 fd1d_heat_implicit.py > fd1d_heat_implicit.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#  Get rid of obnoxious garbage.
#
rm -f *.pyc
rm -rf __pycache__
#
echo "Normal end of execution."
