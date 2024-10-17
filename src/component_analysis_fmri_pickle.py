import numpy as np
from sklearn.decomposition import PCA
from functions_data import unify_scan_sizes
import functions_data
from functions_data import reshape_mri_data_for_pca
# from dictionaries import *
# from dictionaries import 

fmri_filename="/rds/general/user/jp2923/ephemeral/data/fmri_data.pkl"

data_functional = functions_data.load_pickle(fmri_filename)

print("Loaded fmri data")

data_functional = unify_scan_sizes(data_functional)

print("Successfully unified fmri scans!")

# pick single timestep to represent fmri scans
# BOLD signal required, not the whole functional volume
selected_timestep = 1
data_functional_single_timestep = data_functional[:,:,:,selected_timestep]

# Set up Principle Component Analysis for structural and functional data 
pca_fmri = PCA()

# reshape for pca
data_functional_pre_pca = reshape_mri_data_for_pca(data_functional_single_timestep, len(data_functional_single_timestep))

print("Reshaped before pca")

# Perform dimensionality reduction
data_functional_reduced = pca_fmri.fit_transform(data_functional_pre_pca)

print(f"functional data shape: {data_functional_reduced.shape}")

print(f"Explained Variance Ratio (Cumulative, FMRI): {np.cumsum(pca_fmri.explained_variance_ratio_)}")

# Pickle the results for later reuse!!!
fmri_filename="/rds/general/user/jp2923/ephemeral/data/fmri_data_dimred_2.pkl"
functions_data.save_pickle(fmri_filename, data_functional_reduced)