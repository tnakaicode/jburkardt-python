#! /bin/bash
#
python3 average_length.py > average_length_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 game_length.py > game_length_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
python3 one_game.py > one_game_test.txt
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
