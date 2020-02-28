#! /bin/bash
#
python3 data_example.py > data_example_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 hello.py > hello_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 hstack_test.py > hstack_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 main_demo.py > main_demo_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 suppress_spaces.py > suppress_spaces_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 vstack_test.py > vstack_test.txt
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
