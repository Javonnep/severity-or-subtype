# This file was written mostly via Claude AI
# The file synchronises the subject ids and renames the folders for the subjects correctly.

# other lib imports
import os
import pandas as pd
import shutil
import argparse
from dictionaries import collection_order

# Set up the argument parser
parser = argparse.ArgumentParser(description='Script to handle the subject names')
parser.add_argument('abide_dir', type=str, help='The path from root to the abide_ii folder')
args = parser.parse_args()
abide_dir = args.abide_dir

# Initialize the participant number counter
participant_number = 1

# Create a dictionary to store the mapping of old participant IDs to new participant IDs
participant_id_mapping = {}

# Iterate over each collection in the specified order
for collection in collection_order:
    collection_dir = os.path.join(abide_dir, collection)
    
    # Get the path to the phenotypic CSV file in the base directory
    csv_file_path = os.path.join(abide_dir, f"{collection}.csv")
    
    # Get a list of participant folders in the collection, excluding tar.gz files
    participant_folders = [folder for folder in os.listdir(collection_dir) if os.path.isdir(os.path.join(collection_dir, folder)) and not folder.endswith(".tar.gz")] # check
    
    # Sort the participant folders alphabetically
    participant_folders.sort()
    
    # Iterate over each participant folder and rename it
    for folder in participant_folders:
        old_folder_path = os.path.join(collection_dir, folder)
        new_folder_name = f"sub-{participant_number:03d}"
        new_folder_path = os.path.join(collection_dir, new_folder_name)
        
        # Rename the folder
        shutil.move(old_folder_path, new_folder_path)
        
        # Store the mapping of old participant ID to new participant ID
        participant_id_mapping[folder] = new_folder_name
        
        participant_number += 1
    
    # Read the phenotypic CSV file into a DataFrame, keeping the 'SUB_ID' column as string
    df = pd.read_csv(csv_file_path, dtype={'SUB_ID': str})
    
    # Update the participant IDs in the DataFrame
    df['SUB_ID'] = df['SUB_ID'].map(participant_id_mapping)
    
    # Write the updated DataFrame back to the CSV file
    df.to_csv(csv_file_path, index=False)
    
    print(f"Updated participant IDs in {csv_file_path}")

print("Folder renaming and participant ID updating completed.")
