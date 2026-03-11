#! /bin/bash
#
python3 tetrahedron_arbq_rule.py > tetrahedron_arbq_rule.txt
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
