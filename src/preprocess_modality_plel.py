import subprocess as sp
import os
import argparse
from dictionaries import site_subjects_dictionary, site_tr_dict, site_slice_order_dict
import multiprocessing as mp

def run_anat_preproc(args):
    CCS_APP, site_path, SUBJECTS_DIR, sub_id = args
    sp.run([
        "./src/run_anat_preproc.sh", 
        f"{CCS_APP}", 
        f"{site_path}", 
        f"{SUBJECTS_DIR}", 
        f"{sub_id:003}_1"])

def run_func_preproc(args):
    CCS_APP, site_path, SUBJECTS_DIR, tr, slice_order, sub_id = args
    sp.run([
        "./src/run_func_preproc.sh", 
        f"{CCS_APP}", 
        f"{site_path}", 
        f"{SUBJECTS_DIR}", 
        f"{tr}", 
        f"{slice_order}",
        str(1),
        f"{sub_id:003}_1"])

if __name__ == '__main__':

    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Script to preprocess all volumes from a given site')
    parser.add_argument('site', type=str, help='The site to process (e.g., ABIDEII-BNI_1. Use the name given by the Unzipped file)')
    parser.add_argument('site_root_path', type=str, help='$ABIDE_DIR. path/to/abide_ii')
    parser.add_argument('modality', type=str, help='The modality of MRI scan to preprocess (eg s/f)')

    # assign the arguments to variables
    args = parser.parse_args()
    site = args.site
    site_root_path = args.site_root_path
    modality = args.modality

    # path from site
    site_path_dictionary = {
        "ABIDEII-BNI_1":f"{site_root_path}/ABIDEII-BNI_1/CCS",
        # "ABIDEII-EMC_1":f"{site_root_path}/ABIDEII-EMC_1/CCS",
        "ABIDEII-ETH_1":f"{site_root_path}/ABIDEII-ETH_1/CCS",
        "ABIDEII-KUL_3":f"{site_root_path}/ABIDEII-KUL_3/CCS",
        "ABIDEII-KKI_1":f"{site_root_path}/ABIDEII-KKI_1/CCS",
        "ABIDEII-KKI_2":f"{site_root_path}/ABIDEII-KKI_2/CCS",
        "ABIDEII-KKI_3":f"{site_root_path}/ABIDEII-KKI_3/CCS",
        "ABIDEII-KKI_4":f"{site_root_path}/ABIDEII-KKI_4/CCS",
        "ABIDEII-TCD_1":f"{site_root_path}/ABIDEII-TCD_1/CCS",
    }
    # Get the fixed vars
    n_subjects = 12
    site_path = site_path_dictionary[site]
    CCS_APP = os.environ.get("CCS_APP")
    SUBJECTS_DIR = os.environ.get("SUBJECTS_DIR")

    if modality == "a" or modality == "s":
        print("\n=+-ABOUT TO RUN ANAT-+=" * 4)

        with mp.Pool(processes=n_subjects) as pool:
            args = [(CCS_APP, site_path, SUBJECTS_DIR, sub_id) for sub_id in site_subjects_dictionary[site]]
            pool.map(run_anat_preproc, args)

    elif modality == "f":
        print("\n=+-ABOUT TO RUN FUNC-+=" * 4)

        with mp.Pool(processes=n_subjects) as pool:
            args = [(CCS_APP, site_path, SUBJECTS_DIR, site_tr_dict[site], site_slice_order_dict[site], sub_id) 
                    for sub_id in site_subjects_dictionary[site]]
            pool.map(run_func_preproc, args)