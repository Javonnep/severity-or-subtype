#!/bin/bash

# Check if all required arguments are provided
if [ "$#" -ne 7 ]; then
    echo "Usage: $0 <CCS_APP> <CCS_DIR> <SUBJECTS_DIR> <TR> <sliceOrder> <FWHM> <subject>"
    exit 1
fi

# Assign arguments to variables

CCS_APP=$1
CCS_DIR=$2
SUBJECTS_DIR=$3
TR=$4
sliceOrder=$5
FWHM=$6
subject=$7

# subject=$5
# Define CCS_APP (assuming it's constant, otherwise you might want to make this an argument too)
# CCS_APP=/home/javonne/thesis_downloads/CCS

# Create the scripts directory
mkdir -p $CCS_DIR/$subject/scripts/


# Generate the subject-specific script
sed "s/CCSsubjectname/$subject/" $CCS_APP/samplesScripts/template_preproc_funcpart_wargs.sh > $CCS_DIR/$subject/scripts/ccs_preproc_funcpart.sh

# Make the script executable
chmod +x $CCS_DIR/$subject/scripts/ccs_preproc_funcpart.sh

# Run the subject-specific script with arguments
$CCS_DIR/$subject/scripts/ccs_preproc_funcpart.sh "$CCS_APP" "$CCS_DIR" "$SUBJECTS_DIR" "$TR" "$sliceOrder" "$FWHM"