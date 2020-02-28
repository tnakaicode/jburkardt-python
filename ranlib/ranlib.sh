#! /bin/bash
#
#export PYTHONPATH=$PYTHONPATH:/home/burkardt/public_html/py_src/rnglib
export PYTHONPATH=$PYTHONPATH:$HOME/public_html/py_src/rnglib
#
python3 ranlib.py > ranlib.txt
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
