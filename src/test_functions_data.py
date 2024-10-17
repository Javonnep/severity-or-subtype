import os
import numpy as np
import functions_data
from dictionaries import subject_site_dictionary, highest_subject_id
from nilearn import image

# Tests that assume data is stored locally will be commented to allow github action integration

# def test_load_subject_paths():

#     abide_path=f"rds/general/user/jp2923/home/irp-jp2923/data/abide_ii/"
#     smri_path="anat/reg/highres.nii.gz"
    
#     smri_paths = functions_data.load_subject_paths(
#         abide_path=abide_path, 
#         scan_path_post_subject=smri_path, 
#         subject_site_dictionary=subject_site_dictionary, 
#         highest_subject_id=highest_subject_id)

#     # check the 5 of the generated paths exist
#     random_checks = [np.random.randint(0,50) for i in range(5)]

#     for i in random_checks:
#         assert not os.path.exists(smri_paths[i])


# def test_load_scans_from_paths_exists():
#     path = f"../data/abide_ii/sub-046_ses-1_task-rest_bold.nii.gz"
#     # Next line will fail to load if the scan is not present
#     scan_array = image.load_img(path).get_fdata()
#     assert scan_array is not None

# def test_load_scans_from_paths_type():
#     path = f"../data/abide_ii/sub-046_ses-1_task-rest_bold.nii.gz"
#     # Next line will fail to load if the scan is not present
#     scan_array = image.load_img(path).get_fdata()
#     assert type(scan_array) == np.ndarray

def test_unify_scan_sizes():
    # generate some scans with different sizes
    data_functional = [np.random.random(size=(128, 128, 50, 2)) for i in range(2)] + [np.random.random(size=(118, 118, 45, 2))]
    # add all shapes to a set and confirm its length is greater than 1
    initial_shapes = [volume.shape for volume in data_functional]
    assert len(set(initial_shapes)) > 1


    # Unify/Upscale shapes
    data_functional = functions_data.unify_scan_sizes(data_functional)
    # add all shapes to a set and confirm its length is equal to 1
    final_shapes = [volume.shape for volume in data_functional]
    assert len(set(final_shapes)) == 1

def test_reshape_mri_data_for_pca():
    n_subjects = 3
    test_volumes = np.array([np.random.randint(0,100,size=(25,25,25)) for i in range(n_subjects)])
    reshaped_data = functions_data.reshape_mri_data_for_pca(test_volumes, n_subjects)
    assert reshaped_data.shape[0] == n_subjects
    assert reshaped_data.shape[1] == 25**3
    
