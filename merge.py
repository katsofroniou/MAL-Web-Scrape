import json
import os
import shutil

def merge_files(database):
    # Step 1: Create the directory path
    directory_path = f"data/raw/{database}"

    # Step 2: Initialize an empty list to store merged data
    data = []

    # Step 3: Iterate over all the files in the directory
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        with open(filepath, 'r') as file:
            # Load the JSON content from the file and append it to the data list
            data.append(json.load(file))

    # Step 4: Write the merged data into a new JSON file
    merged_filepath = f"data/raw/{database}.json"
    with open(merged_filepath, 'w') as merged_file:
        # Write the merged data with an indentation of 4 for better readability
        json.dump(data, merged_file, indent=4)

    # Step 5: Delete the directory with individual JSON files
    shutil.rmtree(directory_path)

merge_files('anime')
merge_files('manga')