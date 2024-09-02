#!/bin/bash
#SBATCH --ntasks=64
#SBATCH --mem=128G
#SBATCH -J LTX-Li-E-ref-37012
#SBATCH --time=15:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=amaan@pppl.gov


echo $SLURM_NODELIST
echo $SLURM_NTASKS
echo $SLURM_JOBID
echo $SLURM_SUBMIT_DIR
		
time mpirun --verbose -np $SLURM_NTASKS chunks_37012_ltx_ro.o