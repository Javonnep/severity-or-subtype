from dictionaries import highest_subject_id, subject_site_dictionary
from nilearn import image
import numpy as np
import pickle
from scipy.ndimage import zoom

def save_pickle(filename, object_to_pickle):
    """Saves a pickle to storage

    Args:
        filename (str): The filename including the path to save to
        object_to_pickle (Object): The object to save
    """
    with open(filename, "wb") as handle:
        pickle.dump(object_to_pickle, handle)

def load_pickle(filename):

    """Loads a previously saved pickled object
    
    Args:
        filename (str): The filename including the path to load from
    
    Returns:
        Object: The object to lead
    """
    with open(filename, "rb") as f:
        pickled_object = pickle.load(f)
    return pickled_object

def load_subject_paths(abide_path, scan_path_post_subject, subject_site_dictionary, highest_subject_id):
    """A function that creates a list of paths to all scans of MRI volumes

    Args:
        abide_path (str): The path to the abide_ii directory that contains all site folders
        scan_path_post_subject (str): The path to the actual scan. Usually what comes after ...site/CCS/subject
        subject_site_dictionary (dict): A dictionary [key:subject, value:site]
        highest_subject_id (int): The highest subject id number

    Returns:
        _type_: A list of paths to all MRI volumes of a specific type
    """
    paths = [f"/{abide_path}/{subject_site_dictionary[i]}/CCS/{i:03}_1/{scan_path_post_subject}" for i in range(1, highest_subject_id+1)]
    return paths

def load_scans_from_paths(paths):
    """A function that given a list of MRI volume paths, will load all of the volumes into a python list

    Args:
        paths (list[str]): A list of strings

    Returns:
        list[np.Array]: the MRI volumes as numpy arrays in a list of strings
    """
    data = []
    for path in paths:
        try:
            scan_array = image.load_img(path).get_fdata()
            data.append(scan_array)
            print(f"Shape of {path}: {scan_array.shape}")
        except Exception as e:
            print("Missing path!")
            print(e)
            print("Missing path!")
    return data

#===========THE FOLLOWING FUNCTION WAS WRITTEN USING CLAUDE AI==================
# Assuming scans is your list of numpy arrays
# Find the maximum dimensions

def unify_scan_sizes(scans):
    

    """A function that given a python list of numpy arrays, will upscale all arrays to one uniform shape 
    
    Args:
        paths (list[str]): A list of paths to .nii.gz volumes
    
    Returns:
        list[np.Array]: The arrays upscaled to one uniform shape
    """

    # Find the maximum dimensions for the first three dimensions (spatial)
    max_spatial_dims = np.max([scan.shape[:3] for scan in scans], axis=0)
    
    # Find the minimum time dimension
    min_time_dim = min(scan.shape[3] for scan in scans)
    
    unified_scans = []
    
    for scan in scans:
        # Calculate zoom factors for spatial dimensions
        spatial_factors = [max_dim / dim for max_dim, dim in zip(max_spatial_dims, scan.shape[:3])]
        
        # Add 1 as the zoom factor for the time dimension (no zooming)
        factors = spatial_factors + [1]
        
        # Apply zoom
        zoomed_scan = zoom(scan, factors, order=1)  # order=1 for linear interpolation
        
        # Truncate the time dimension
        truncated_scan = zoomed_scan[..., :min_time_dim]
        
        unified_scans.append(truncated_scan)

    return np.array(unified_scans)
#===========END OF CLAUDE AI CODE==================

def reshape_mri_data_for_pca(volumes, n_participants):
    """Given an array of mri volumes, this will reshape it to prepare for pca

    Args:
        volumes (list[np.Array]): A list of MRI volumes represented by Numpy Arrays.
        n_participants (int): The number of participants in the list

    Returns:
        _type_: The list, but now ready to undergo dimensionality reduction with PCA
    """

    
    # From SKLEARN DOCUMENTATION: X {array-like, sparse matrix} of shape (n_samples, n_features)
    return volumes.reshape(n_participants, -1)

if __name__ == "__main__":

    abide_path=f"rds/general/user/jp2923/home/irp-jp2923/data/abide_ii/"
    fmri_path="rest/rest_pp_nofilt_sm0.nii.gz"
    smri_path="anat/reg/highres.nii.gz"

    fmri_paths = load_subject_paths(
            abide_path=abide_path, 
            scan_path_post_subject=fmri_path, 
            subject_site_dictionary=subject_site_dictionary, 
            highest_subject_id=highest_subject_id)
    
    smri_paths = load_subject_paths(
            abide_path=abide_path, 
            scan_path_post_subject=smri_path, 
            subject_site_dictionary=subject_site_dictionary, 
            highest_subject_id=highest_subject_id)
    
    smri_data = load_scans_from_paths(smri_paths)
    fmri_data = load_scans_from_paths(fmri_paths)

    smri_filename="/rds/general/user/jp2923/ephemeral/data/smri_data.pkl"
    fmri_filename="/rds/general/user/jp2923/ephemeral/data/fmri_data.pkl"

    save_pickle(smri_filename, smri_data)
    save_pickle(fmri_filename, fmri_data)