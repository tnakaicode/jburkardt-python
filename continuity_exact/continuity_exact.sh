#! /bin/bash
#
python3 continuity_exact.py > continuity_exact.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
gnuplot < continuity_exact_commands.txt
#
#  Get rid of obnoxious garbage.
#
rm -f *.pyc
rm -rf __pycache__
#
echo "Normal end of execution."
