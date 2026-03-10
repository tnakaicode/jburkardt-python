#! /bin/bash
#
python3 gauss_seidel_stochastic.py >& gauss_seidel_stochastic.txt
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
