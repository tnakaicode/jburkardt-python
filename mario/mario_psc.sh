#! /bin/bash
#
#SBATCH --gres=gpu:k80:4
#SBATCH -J mario_psc
#SBATCH -N 1
#SBATCH --ntasks-per-node 4
#SBATCH --output=mario_psc.log
#SBATCH -p GPU
#SBATCH -t 0:01:00
#
set -x
#
#  Set up the environment.
#
module load anaconda3/2019.03
source activate keras-gpu
#
#  Run the program.
#
python3 mario.py > mario_psc.txt
#
echo "Normal end of execution."
