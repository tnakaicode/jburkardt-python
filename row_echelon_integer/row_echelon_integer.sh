#! /bin/bash
#
python3 row_echelon_integer.py > row_echelon_integer.txt
if [ $? -ne 0 ]; then
  echo "Runtime errors."
  exit 1
fi
#
#  Get rid of obnoxious garbage.
#
rm -f *.pyc
rm -rf __pycache__
#
echo "Normal end of execution."
