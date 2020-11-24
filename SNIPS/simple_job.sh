#!/bin/bash
#SBATCH --cpus-per-task=8
#SBATCH --mem=30000M
#SBATCH --gres=gpu:1
#SBATCH --time=0-28:00
#SBATCH --output=try_bi_rnn.out

python train.py 
