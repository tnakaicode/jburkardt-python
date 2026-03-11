#! /bin/bash
#
python3 random_walk_2d_avoid_simulation.py > random_walk_2d_avoid_simulation.txt
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
