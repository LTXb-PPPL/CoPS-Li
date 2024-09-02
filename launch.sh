#!/bin/bash
#SBATCH --ntasks=512
#SBATCH --mem=128G
#SBATCH -J LTX-Li-E-src-233
#SBATCH --time=04:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=amaan@pppl.gov

echo $SLURM_NODELIST
echo $SLURM_NTASKS
echo $SLURM_JOBID
echo $SLURM_SUBMIT_DIR
		
time mpirun --verbose -np $SLURM_NTASKS chunks_233_ltx_so.o