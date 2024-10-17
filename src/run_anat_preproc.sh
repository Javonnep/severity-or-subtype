#!/bin/bash

# Check if all required arguments are provided
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <CCS_APP> <CCS_DIR> <SUBJECTS_DIR> <subject>"
    exit 1
fi

export CCS_APP=$1
export CCS_DIR=$2
export SUBJECTS_DIR=$3
export subject=$4

$CCS_APP/H1/ccs_anat_01_pre_freesurfer.sh "$CCS_DIR" "$SUBJECTS_DIR" "$subject"
$CCS_APP/H1/ccs_anat_02_freesurfer.sh "$CCS_DIR" "$SUBJECTS_DIR" "$subject"
$CCS_APP/H1/ccs_anat_03_postfs.sh "$CCS_DIR" "$SUBJECTS_DIR" "$subject"