#! /bin/bash
#
g++ -c -Wall mesh_bandwidth.cpp
if [ $? -ne 0 ]; then
  echo "Compile error."
  exit
fi
#
g++ mesh_bandwidth.o
if [ $? -ne 0 ]; then
  echo "Load error."
  exit
fi
rm mesh_bandwidth.o
#
chmod ugo+x a.out
mv a.out ~/bincpp/mesh_bandwidth
#
echo "Normal end of execution."
