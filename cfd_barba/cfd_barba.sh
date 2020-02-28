#! /bin/bash
#
python3 step01.py > step01_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 step02.py > step02_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 step03.py > step03_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 step04.py > step04_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 step05.py > step05_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 step06.py > step06_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 step07.py > step07_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 step08.py > step08_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 step09.py > step09_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 step10.py > step10_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 step11.py > step11_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 step12.py > step12_test.txt
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
