#!/bin/bash

# Check if all required arguments are provided
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <CCS_APP> <CCS_DIR> <SUBJECTS_DIR> <subject>"
    exit 1
fi

CCS_APP=$1
CCS_DIR=$2
SUBJECTS_DIR=$3
subject=$4

$CCS_APP/H1/ccs_01_dtipreproc.sh "$subject" "$CCS_DIR" dti dti anat
$CCS_APP/H1/ccs_02_dtibbregister.sh "$subject" "$CCS_DIR" dti dti fsaverage5 "$SUBJECTS_DIR"
$CCS_APP/H1/ccs_03_dtisegment.sh "$subject" "$CCS_DIR" dti