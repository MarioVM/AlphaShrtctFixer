import os
import winshell
import logging
from tqdm import tqdm
from datetime import datetime

# Set up logging
logging.basicConfig(filename='alphascf.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Get the current folder path
current_folder = os.path.dirname(os.path.abspath(__file__))

# Get all the files in the current folder
files = os.listdir(current_folder)

# Create a progress bar
progress_bar = tqdm(total=len(files), position=0, leave=True)

# Initialize a flag to check if any changes were made
changes_made = False

# Iterate over all the files in the current folder
for file_name in files:
    file_path = os.path.join(current_folder, file_name)

    # Check if the file is a shortcut
    if file_path.lower().endswith('.lnk'):
        try:
            # Get the shortcut object
            shortcut = winshell.shortcut(file_path)

            # Get the current target and start in paths
            target_path = shortcut.path
            start_in_path = shortcut.working_directory

            # Change the drive letters to "W"
            new_target_path = target_path.replace(target_path[0], 'W')
            new_start_in_path = start_in_path.replace(start_in_path[0], 'W')

            # Check if the new paths exist
            if os.path.exists(new_target_path) and os.path.exists(new_start_in_path):
                final_target_path = new_target_path
                final_start_in_path = new_start_in_path
            else:
                # Change the drive letters to "F" if "W" doesn't work
                final_target_path = target_path.replace(target_path[0], 'F')
                final_start_in_path = start_in_path.replace(start_in_path[0], 'F')

            # Check if any changes were made
            if final_target_path != target_path or final_start_in_path != start_in_path:
                changes_made = True

                # Update the shortcut with the new paths
                shortcut.path = final_target_path
                shortcut.working_directory = final_start_in_path
                shortcut.write()  # Use write() to save changes

                logging.info
