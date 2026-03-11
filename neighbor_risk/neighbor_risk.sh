#! /bin/bash
#
python3 neighbor_risk.py > neighbor_risk.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
mv neighbor_risk neighbor_risk.dot
#
#  Get rid of obnoxious garbage.
#
rm -f *.pyc
rm -rf __pycache__
#
echo "Normal end of execution."
