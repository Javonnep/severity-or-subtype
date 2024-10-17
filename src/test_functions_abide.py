import functions_abide as fa
import numpy as np
import pandas as pd

def test_allign_cluster_label_with_asd_ids():
    
    dx_indecies_asd = [0,2,3,5]
    labels = [1,0,0,1]
    # 'DX_GROUP': [1,2,1,1,2,1],

    # converting to df is not efficient, but is how I will use the code in practice
    data = {"labels":[1,-1,0,0,-1,1]}
    df = pd.DataFrame(data)
    # convert to 1d df
    df_to_arr_reshaped = np.array(df).reshape(1,-1)[0]
    assert np.all(df_to_arr_reshaped == fa.allign_cluster_label_with_asd_ids(dx_indecies_asd,labels,6))


def test_get_dx_indexes():
    data = {       
        'DX_GROUP': [1,2,1,1,2,1],
    }
    df = pd.DataFrame(data)
    dx_indecies_asd = fa.get_dx_indexes(df, which="asd")
    dx_indecies_all = fa.get_dx_indexes(df, which="all")

    assert dx_indecies_asd == [0,2,3,5]
    assert dx_indecies_all == [1,4]

def test_nan_ratio_col():

    data = {       
        'ID': ["sub-001", "sub-002", "sub-003", "sub-004"],
        'Group': [0, 1, 0, np.nan],
        'Handedness': ['l', 'r', np.nan, np.nan],
        'fav_food': [np.nan, np.nan, np.nan, np.nan]
    }
    df = pd.DataFrame(data)
    
    assert fa.nan_ratio_col(df,"ID") == 0.0 
    assert fa.nan_ratio_col(df,"Group") == 0.25
    assert fa.nan_ratio_col(df,"Handedness") == 0.5 
    assert fa.nan_ratio_col(df,"fav_food") == 1.0 

# find_elbow is verified visually 
