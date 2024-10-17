# imports 
import numpy as np
from dictionaries import *
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def scatter_plot(data, title, xl=None, yl=None, colours=None):
    """_summary_

    Args:
        data (list[list[int], list[int]]): The data that you want to plot. data=[X, y] 
        title (str): The title of the plot
        xl (str, optional): The label of the x-axis. Defaults to None.
        yl (str, optional): The label of the y-axis. Defaults to None.
        colours (list[int], optional): The labels by which you colour the plot. Defaults to None.
    """
    plt.scatter(data[0], data[1], c=colours)
    plt.title(title)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.tight_layout()
    plt.xticks([])
    plt.yticks([])
    plt.show()

#===========THE FOLLOWING FUNCTION WAS WRITTEN USING CLAUDE AI==================
def allign_cluster_label_with_asd_ids(asd_indices, labels, total_subjects):
    """A function that takes you from _ > _

    Args:
        asd_indices (list[int]): A list of index values that represent the index of each autistic participant in your df/list
        labels (list[int]): The cluster labels of the autistic subjects
        total_subjects (int): The total number of subjects in your sample

    Returns:
        list[int]: A list containing an integer to represent which cluster an autistic person belongs to, with -1 to represent the cluster of non-autistic subjects
    """
    harmonised_labels = [-1] * total_subjects  # Initialize all labels to -1
    
    for i, label in zip(asd_indices, labels):
        harmonised_labels[i] = label
    
    return harmonised_labels

# written with claude ai
# Function to find the elbow point
def find_elbow(wcss):
    """Finds the elbow point telling you how many clusters to use in Kmeans clustering

    Args:
        wcss (list[int]): A list of the (W)ithin (C)luster (S)um of (S)quares for each k value tested.

    Returns:
        int: The optimal K value
    """
    differences = np.diff(wcss)
    acceleration = np.diff(differences)
    elbow_index = np.argmax(acceleration) + 2
    return elbow_index


# written with claude ai
def elbow_plot_clustering(data, max_clusters=15):
    """Plots an elbow plot for KMeans clustering optimal K detection

    Args:
        data (list[list[int], list[int]]): The data you want to cluster. data=[X, y]
        max_clusters (int, optional): The maximum number of clusters you want to try. Defaults to 15.

    Returns:
        list[int]: A list of the (W)ithin (C)luster (S)um of (S)quares for each k value tested.
    """
    wcss = []

    for k in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, max_iter=300, n_init=10, random_state=0)
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)

    # Plot the Elbow curve
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, max_clusters + 1), wcss, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('WCSS')
    plt.show()

    return wcss
#===========END OF CLAUDE AI CODE==================

def get_dx_indexes(df_with_dx, which="asd"):
    """A function that converts the diagnostic group from a dataframe to a list.

    Args:
        df_with_dx (pandas.DataFrame): A DataFrame that has the column "DX_GROUP" form the ABIDE phenotypic dataset.
        which (str, optional): Which group you want. Either asd for autistic patients, or all for allistic patients. Defaults to "asd".

    Raises:
        Exception: If you pick an invalid DX group, an exception will be raised. Options are "asd" or "all"

    Returns:
        _type_: _description_
    """
    df_with_dx["DX_GROUP"]
    asd_indexes = []
    all_indexes = []

    for index in range(len(df_with_dx)):
        
        if df_with_dx["DX_GROUP"].iloc[index] == 1:
            asd_indexes.append(index)

        elif df_with_dx["DX_GROUP"].iloc[index] == 2:
            all_indexes.append(index)
    
    if which == "asd" or which == 1:
        return asd_indexes
    elif which == "all" or which == 2:
        return all_indexes
    else:
        raise Exception("Invalid dx group selected")
    
# This function was written by me during the DSML module of the ACSE course.
def nan_ratio_col(df, col):
    """Gives you the nan rate for a column

    Args:
        df (pandas.DataFrame): The DataFrame you want to investigate
        col (str): The column you want to investigate

    Returns:
        float: the rate of nans in the column in the DataFrame
    """
    nan_ratio = sum(df[col].isna()) / len(df[col])
    return nan_ratio

#===========NOTES FOR THE FOLLOWING CODE==================
# The basic plotting code for theses functions was written with Claude ai
# However I developed the design of the functions and aestetics of the plots
def create_boxplot(data, trait_name):
    """Plots a boxplot

    Args:
        data (list[pandas.DataFrame, pandas.DataFrame]): The data you want a boxplot for. data=[sample 1, sample 2]
        trait_name str): The column title within the dartaframes that you want boxplots for.
    """
    # The initial plotting code comes from claude ai but was editted by me
    # Create a figure and axis
    _, ax = plt.subplots(figsize=(10, 6))

    # Create the boxplot
    # box_plot = ax.boxplot([C1_IQ, C2_IQ, C3_IQ[~np.isnan(C3_IQ)]], patch_artist=True)
    box_plot = ax.boxplot([data[0][~np.isnan(data[0])], data[1][~np.isnan(data[1])]], patch_artist=True)

    # Customize the plot
    ax.set_title(f'{trait_name} of detected clusters')
    ax.set_xlabel('Clusters')
    ax.set_ylabel(f'{trait_name}')
    ax.set_xticklabels(['cluster 0', 'cluster 1'])

    # Customize colors
    colors = ['lightblue', 'lightgreen']
    for patch, color in zip(box_plot['boxes'], colors):
        patch.set_facecolor(color)

    # Add a grid for better readability
    ax.yaxis.grid(True)

    # Show the plot
    plt.tight_layout()
    plt.show()

def plot_histogram(data, trait_name, binsize=10):
    """Plots a histogram

    Args:
        data (list[pandas.DataFrame, pandas.DataFrame]): The data you want a boxplot for. data=[sample 1, sample 2]
        trait_name str): The column title within the dartaframes that you want boxplots for.
        binsize (int, optional): The size of the histograms bins. Defaults to 10.
    """
    # Create the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(data[0], bins=binsize, alpha=0.5, label='Cluster 0')
    plt.hist(data[1], bins=binsize, alpha=0.5, label='Cluster 1')

    # Customize the plot
    plt.title(f'{trait_name} of detected clusters')
    plt.xlabel(trait_name)
    plt.ylabel('Frequency')
    plt.legend()

    # Display the plot
    plt.show()
#===========END OF BLOCK==================

if __name__ == "__main__":
    # print(get_participant_information(pid=25))
    # print(id_int_to_str(200))

    import pandas as pd
    dx_indecies_asd = [0,2,3,5]
    labels = [1,0,0,1]
    data = {"labels":[1,-1,0,0,-1,1]}
    df = pd.DataFrame(data)
    print(np.array(df).reshape(1,-1)[0])
    print(allign_cluster_label_with_asd_ids(dx_indecies_asd,labels,6))
    pass