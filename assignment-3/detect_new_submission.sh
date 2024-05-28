#!/bin/bash

# NOTE: THIS IS ONLY SPECIFIC TO THE CURRENT ASSIGNMENT

studentFoldersBase="/home/me123/markben/students-home"
assignment="assignment-3"
recordedSubmissionsDir="/home/me123/markben/scripts/assignment-3/recorded-submissions"
mkdir -p "$recordedSubmissionsDir"

# process each student folder
for studentDir in "$studentFoldersBase"/*; do
    studentId=$(basename "$studentDir")

    # loop through each submission directory for the student
    for submissionDir in "$studentDir/$assignment/submission-"*; do
        # skip if no directories are found
        [ -d "$submissionDir" ] || continue

        submissionNumber=$(basename "$submissionDir")
        recordFile="$recordedSubmissionsDir/${studentId}-${submissionNumber}"

        # check if this submission is already processed
        if [ ! -f "$recordFile" ]; then
            # create an empty file to record this submission as processed
            touch "$recordFile"
            # not processed, so process now
            /home/me123/markben/scripts/assignment-3/prep_and_run_submission.sh "$submissionDir"
        fi
    done
done

