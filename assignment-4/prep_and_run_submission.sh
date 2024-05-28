#!/bin/bash

cwd="$1"
# extract the relevant suffix starting from "students-home"
path_suffix="${cwd#*/markben/}"
new_dir="$HOME/local-${path_suffix}"
# create local directory
mkdir -p "$new_dir"
# move files into local directory
cp "$cwd/responses.txt" "$new_dir"
cd "$new_dir"
cp /home/me123/markben/scripts/assignment-4/parse_refinements.py "$new_dir"

# just to shake things up
delay=$((120 + RANDOM % 301))
sleep $delay

output=$(python3 parse_refinements.py)
# copy the image file to the desired location
cp "/home/me123/markben/new-hw4/simulations/${output}/data.tar.gz" "$cwd"
cp "/home/me123/markben/new-hw4/simulations/${output}/probes.tar.gz" "$cwd"
cp "/home/me123/markben/assignment-starters/assignment-4/README.txt" "$cwd"

# generate input files
#job_output=$(sbatch job.slurm)
#job_id=$(echo $job_output | awk '{print $4}')  # 4th word should be job ID
#
## wait for job to complete
#while squeue | grep -q "$job_id"; do
#    sleep 1
#done

# run
# post-processing
#cp ./output.txt "$cwd"
