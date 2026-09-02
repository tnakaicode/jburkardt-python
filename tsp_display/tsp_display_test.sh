#! /bin/bash
#
matlab -nodisplay -nosplash -nodesktop -batch \
  "run('tsp_display_test.m');exit;" > tsp_display_test.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit
fi
#
echo "Normal end of execution."
