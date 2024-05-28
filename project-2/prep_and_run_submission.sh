#!/bin/bash

cwd="$1"
# extract the relevant suffix starting from "students-home"
path_suffix="${cwd#*/markben/}"
new_dir="$HOME/local-${path_suffix}"
# create local directory
mkdir -p "$new_dir"
# move files into local directory
cp "$cwd/file.tar.gz" "$new_dir"
cd "$new_dir"
tar -xvzf file.tar.gz
cp /home/me123/markben/assignment-starters/project-2/* .
source ~/.bashrc
conda activate me123
python3 check_bbox.py
# rename zone to MAP
#awk 'NR==1{$2="WALL"; print $1, $2; next} /^  endsolid/{print "  endsolid WALL"; next} 1' wing.stl > temp.stl && mv temp.stl wing.stl
awk 'NR==1{$2="WALL"; for(i=3;i<=NF;i++) $i=""; print; next} /^  endsolid/{print "  endsolid WALL"; next} 1' wing.stl > temp.stl && mv temp.stl wing.stl

# generate input files
#python3 run_stl_checks.py
job_output=$(sbatch cpu.slurm)
job_id=$(echo $job_output | awk '{print $4}')  # 4th word should be job ID

# wait for job to complete
while squeue | grep -q "$job_id"; do
    sleep 1
done

# run
# post-processing

job_output=$(sbatch gpu.slurm)
job_id=$(echo $job_output | awk '{print $4}')  # 4th word should be job ID

# wait for job to complete
while squeue | grep -q "$job_id"; do
    sleep 1
done

# run
# post-processing
cp ./job.cpu.out "$cwd"
cp ./job.gpu.out "$cwd"
cp ./error.cpu.out "$cwd"
cp ./error.gpu.out "$cwd"
tar -cvzf data.tar.gz data
tar -cvzf images.tar.gz images
cp data.tar.gz "$cwd"
cp images.tar.gz "$cwd"
cp stl_error.txt "$cwd"
#rm -rf *
