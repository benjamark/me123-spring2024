#!/bin/bash

cwd="$1"
# extract the relevant suffix starting from "students-home"
path_suffix="${cwd#*/markben/}"
new_dir="$HOME/local-${path_suffix}"
# create local directory
mkdir -p "$new_dir"
# move files into local directory
cp "$cwd/file.stl" "$new_dir"
cd "$new_dir"
#mv "*.stl" "file.stl"
cp /home/me123/markben/scripts/assignment-1/run_stl_checks.py .
cp /home/me123/markben/assignment-starters/assignment-1/* .
# generate input files
#python3 run_stl_checks.py
job_output=$(sbatch job.slurm)
job_id=$(echo $job_output | awk '{print $4}')  # 4th word should be job ID

# wait for job to complete
while squeue | grep -q "$job_id"; do
    sleep 1
done

# run
# post-processing
cp ./output.txt "$cwd"
