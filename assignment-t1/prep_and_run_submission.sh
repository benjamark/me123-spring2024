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
cp /home/me123/markben/scripts/assignment-t1/parse_responses.py .
cp /home/me123/markben/assignment-starters/assignment-t1/* .
# generate input files
python3 parse_responses.py
# run
job_output=$(sbatch job.slurm)
job_id=$(echo $job_output | awk '{print $4}')  # 4th word should be job ID

# wait for job to complete
while squeue | grep -q "$job_id"; do
    sleep 1
done

# post-processing
/home/me123/markben/software/ffmpeg/bin/ffmpeg -framerate 12 -pattern_type glob -i 'data/images/*.png' -c:v mpeg4 -pix_fmt yuv420p output.mp4
cp ./output.mp4 "$cwd"
cp ./images/mesh.png "$cwd"
cp ./job.*.out "$cwd"
cp ./error.*.out "$cwd"
cp ./data/forces/forces.dat "$cwd"
