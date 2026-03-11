#! /bin/bash
#
python3 peaks_movie.py > peaks_movie.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
convert -delay 10 -loop 1 peaks_frame*.png peaks_movie.gif
if [ $? -ne 0 ]; then
  echo "GIF creation error."
  exit 1
fi
echo "Animation created as 'peaks_movie.gif'."
rm *.png
#
#  Get rid of obnoxious garbage.
#
rm -f *.pyc
rm -rf __pycache__
#
echo "Normal end of execution."
