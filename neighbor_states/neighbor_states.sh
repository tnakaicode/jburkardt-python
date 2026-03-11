#! /bin/bash
#
python3 neighbor_states.py > neighbor_states.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
mv neighbor_states neighbor_states.dot
#
#  Get rid of obnoxious garbage.
#
rm -f *.pyc
rm -rf __pycache__
#
echo "Normal end of execution."
