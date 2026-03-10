#! /bin/bash
#
echo "Skip execution of gray_scott_movie.  It can take 45 minutes!"
exit
#
python3 gray_scott_movie.py > gray_scott_movie.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
convert -delay 10 -loop 1 gray_scott_movie*.png gray_scott_movie.gif
if [ $? -ne 0 ]; then
  echo "GIF creation error."
  exit 1
fi
#
#  Get rid of obnoxious garbage.
#
rm -f *.pyc
rm -rf __pycache__
#
echo "Normal end of execution."
