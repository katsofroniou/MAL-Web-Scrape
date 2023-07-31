import json
import os
import shutil

def merge_files(database):
    directory_path = f"data/raw/{database}"

    # empty list to store all data
    data = []

    # Iterate over all the files
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        with open(filepath, 'r') as file:

            # Load the JSON content + append it to list
            data.append(json.load(file))

    # Write to new JSON
    merged_filepath = f"data/raw/{database}.json"
    with open(merged_filepath, 'w') as merged_file:

        # better readability
        json.dump(data, merged_file, indent=4)

    # Delete individual files
    shutil.rmtree(directory_path)

merge_files('anime')
merge_files('manga')