import os
import shutil
import argparse
from dictionaries import collection_order
# Set up the argument parser
parser = argparse.ArgumentParser(description='Script to handle the BIDS formatting other than the participant names')
parser.add_argument('abide_dir', type=str, help='The path from root to the abide_ii folder')
args = parser.parse_args()
abide_dir = args.abide_dir

# Initialize the subject/session number counters
subject_number = 1

# loop over collections
for collection in collection_order:
    collection_dir = os.path.join(abide_dir, collection)
    print(f"We are in collection {collection}")

    ## rename sessions 

    # sorting to synchronise with ids    
    # subjects have the correct names
    subject_folders = [folder for folder in os.listdir(collection_dir) if os.path.isdir(os.path.join(collection_dir, folder)) and not folder.endswith(".tar.gz")] 
    subject_folders.sort()
    
    # loop over particpants in a given collection
    for subject in subject_folders:

        # store the original subject name for later
        original_subject_name = subject
        
        # get the subject path
        subject_path = os.path.join(collection_dir, subject)
        # last thing we do before moving onto the next subject
        
        for session in os.listdir(subject_path):

            # get the session path
            session_path = os.path.join(subject_path, session)            

            # rename sessions to ses_0N
            list_session_path = session_path.split("/")[:-1]
            new_session_path = f"{'/'.join(list_session_path)}/ses-1"


            # rename the path before changing the str
            shutil.move(session_path, new_session_path)
            session_path = new_session_path
            
            session = "ses-1"

            # next time we use the subject number it will be for the next subject
            subject_number += 1

            for modality in os.listdir(session_path):

                modality_path = os.path.join(session_path, modality)

                # remove _1 from modalities
                new_modality = f"{modality.split('_')[0]}"
                
                # rename modalities dti>dwi
                if new_modality == 'dti':
                    new_modality = 'dwi'
                elif new_modality == 'rest':
                    new_modality = 'func'
                # new modality folder name
                modality_path_new = os.path.join(session_path, new_modality)
                
                # rename modalities
                shutil.move(modality_path, modality_path_new)

                # change str variables
                modality = new_modality
                modality_path_old = modality_path
                modality_path = modality_path_new

                session_number = 0

                for scan in os.listdir(modality_path):
                    
                    # init 
                    new_scan = None
                    is_bvec = None
                    is_bval = None
                    
                    # original scan filename
                    scan_path = os.path.join(modality_path, scan)
                    #get new scan filenames for:
                    #   fmri
                    if modality == "func":
                        new_scan = f"{subject}_{session}_task-rest_bold.nii.gz"
                    #   smri
                    elif modality == "anat":
                        # all sites are T1w
                        new_scan = f"{subject}_{session}_T1w.nii.gz"
                    
                    #   dti
                    elif modality == "dwi":
                        is_dti = True

                        # scan case
                        if scan.endswith('.nii.gz'):
                            new_scan = f"{subject}_{session}_DWI.nii.gz"
                        
                        elif scan.endswith("bvec"):
                            is_bvec = True
                            bvec = f"{subject}_{session}_DWI.bvec"

                        elif scan.endswith("bval"):
                            is_bval = True
                            bval = f"{subject}_{session}_DWI.bval"

                    else:
                        pass

                    if new_scan:
                        # get the updated name of the scan file
                        scan = new_scan

                        # get the scan path with the new scan name
                        scan_path_new = os.path.join(modality_path, scan)

                        # rename the file (which uses the root)
                        shutil.move(scan_path, scan_path_new)
                        
                        # update the str variable
                        scan_path = scan_path_new
                    
                    if is_bvec:
                        bvec_new_path = os.path.join(modality_path, bvec)
                        bvp = scan_path.split("/")[:-3]
                        bvp.append(session)
                        bvp.append(modality)
                        old_path = os.path.join("/".join(bvp), "dti.bvec")
                        shutil.move(old_path, bvec_new_path)
                    
                    if is_bval:
                        bval_new_path = os.path.join(modality_path, bval)
                        bvap = scan_path.split("/")[:-3]
                        bvap.append(session)
                        bvap.append(modality)
                        old_path = os.path.join("/".join(bvap), "dti.bval")
                        shutil.move(old_path, bval_new_path)