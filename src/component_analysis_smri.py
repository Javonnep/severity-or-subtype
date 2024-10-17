import numpy as np
from sklearn.decomposition import PCA
import pickle
from dictionaries import subject_site_dictionary, highest_subject_id
import functions_data

abide_path=f"rds/general/user/jp2923/home/irp-jp2923/data/abide_ii/"
smri_path="anat/reg/highres.nii.gz"

smri_paths = functions_data.load_subject_paths(
        abide_path=abide_path, 
        scan_path_post_subject=smri_path, 
        subject_site_dictionary=subject_site_dictionary, 
        highest_subject_id=highest_subject_id)

smri_data = functions_data.load_scans_from_paths(smri_paths)

# limit the z axis to ensure data fits in pca object
data_structural = np.array(smri_data)[:,:,::4]

print("Loaded smri data")
print("Shrunk the z axis")

# Set up Principle Component Analysis for structural and functional data 
pca_smri = PCA()

# reshape for pca
data_structural_pre_pca = functions_data.reshape_mri_data_for_pca(data_structural, len(data_structural))

print("Reshaped before pca")

# Perform dimensionality reduction
data_structural_reduced = pca_smri.fit_transform(data_structural_pre_pca)

print(f"structural data shape: {data_structural_reduced.shape}")

print(f"Explained Variance Ratio (Cumulative, SMRI): {np.cumsum(pca_smri.explained_variance_ratio_)}")

# Pickle the results for later reuse!!!
smri_filename="/rds/general/user/jp2923/ephemeral/data/smri_data_dimred_1.pkl"
with open(smri_filename, "wb") as handle:
    pickle.dump(data_structural_reduced, handle)