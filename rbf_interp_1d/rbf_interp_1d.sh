#! /bin/bash
#
export PYTHONPATH=$PYTHONPATH:$HOME/public_html/py_src/test_interp
#
python3 rbf_interp_1d.py > rbf_interp_1d.txt
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
