from neuroCombat import neuroCombat
import pandas as pd
import numpy as np
from dictionaries import site_id_dict, tr_id_dict, site_tr_dict, subject_site_dictionary
import functions_data

sites = []
for _, site in subject_site_dictionary.items():
    sites.append(site_id_dict[site])

#
trs = []
for _, site in subject_site_dictionary.items():
    trs.append(tr_id_dict[site_tr_dict[site]])

uncombatted_data="../data/abide_ii/smri_data_dimred_1.pkl"
data = functions_data.load_pickle(uncombatted_data)


#===========THE FOLLOWING CODE WAS WRITTEN USING CLAUDE AI==================
print("*"*300)
print(data.shape)
print("*"*300)
n_components = data[0].shape[0]  # Number of PCA components
n_participants = len(data)  # Total number of participants

# Create the reshaped matrix
data_matrix = np.zeros((n_components, n_participants))

# Fill the matrix
for i in range(n_participants):
    data_matrix[:, i] = data[i]
#===========END OF CLAUDE AI CODE==================


# The things we want to control for
covars = {
    'site':sites,
    # 'tr':trs
}

covars = pd.DataFrame(covars)

# To specify the name of the variable that encodes for the scanner/batch covariate:
batch_col = 'site'

#Harmonization step:
data_combat = neuroCombat(
    dat=data,
    covars=covars,
    batch_col=batch_col)["data"]

functions_data.save_pickle("../data/abide_ii/smri_data_dimred_combat.pkl",data)