#! /bin/bash
#
python3 lorenz_ode_sensitivity_test.py > lorenz_ode_sensitivity_test.txt
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
