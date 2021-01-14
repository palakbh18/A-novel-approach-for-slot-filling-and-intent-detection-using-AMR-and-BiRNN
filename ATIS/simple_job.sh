#!/bin/bash
#SBATCH --cpus-per-task=8
#SBATCH --mem=30000M
#SBATCH --gres=gpu:1
#SBATCH --time=0-40:00
#SBATCH --output=RNN_200.out

python train.py 
