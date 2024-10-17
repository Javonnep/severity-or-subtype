"""
This file contains important variable and mainly dictionaries for the rest of the project
"""

# ABIDE II
highest_subject_id = 376

# Define the order of the collections
collection_order = [
    "ABIDEII-BNI_1",
    "ABIDEII-ETH_1",
    "ABIDEII-KUL_3",
    "ABIDEII-KKI_1",
    "ABIDEII-KKI_2",
    "ABIDEII-KKI_3",
    "ABIDEII-KKI_4",
    "ABIDEII-TCD_1",
]

## Create the dictionaries
subject_site_dictionary = {
    i:   "ABIDEII-BNI_1" if 1 <= i <= 58
    else "ABIDEII-ETH_1" if 59 <= i <= 95
    else "ABIDEII-KUL_3" if 96 <= i <= 123
    else "ABIDEII-KKI_1" if 124 <= i <= 173
    else "ABIDEII-KKI_2" if 174 <= i <= 223
    else "ABIDEII-KKI_3" if 224 <= i <= 273
    else "ABIDEII-KKI_4" if 274 <= i <= 334
    else "ABIDEII-TCD_1" if 335 <= i <= highest_subject_id
    else Exception for i in range(1, highest_subject_id+1)
}

# ******************* This snippit was written wih Claude AI
# Reverse the subject_site dictionary
site_subjects_dictionary = {}
for key, value in subject_site_dictionary.items():
    if value not in site_subjects_dictionary:
        site_subjects_dictionary[value] = []
    site_subjects_dictionary[value].append(key)
# ******************* End of code written wih Claude AI

site_tr_dict = {
    "ABIDEII-BNI_1":3,
    "ABIDEII-ETH_1":2,
    "ABIDEII-KUL_3":2.5,
    "ABIDEII-KKI_1":2.5,
    "ABIDEII-KKI_2":2.5,
    "ABIDEII-KKI_3":2.5,
    "ABIDEII-KKI_4":2.5,
    "ABIDEII-TCD_1":2,
}

site_slice_order_dict = {
    "ABIDEII-BNI_1":"seq+z",
    "ABIDEII-ETH_1":"seq-z",
    "ABIDEII-KUL_3":"seq+z",
    "ABIDEII-KKI_1":"seq+z",
    "ABIDEII-KKI_2":"seq+z",
    "ABIDEII-KKI_3":"seq+z",
    "ABIDEII-KKI_4":"seq+z",
    "ABIDEII-TCD_1":"seq+z",
}

site_id_dict = {
    "ABIDEII-BNI_1":1,
    "ABIDEII-ETH_1":2,
    "ABIDEII-KUL_3":3,
    "ABIDEII-KKI_1":4,
    "ABIDEII-KKI_2":4,
    "ABIDEII-KKI_3":4,
    "ABIDEII-KKI_4":4,
    "ABIDEII-TCD_1":5,
}

tr_id_dict = {
    2:1,
    2.5:2,
    3:3,
}
