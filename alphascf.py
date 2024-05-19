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

      # Check if any changes were made
      if new_target_path != target_path or new_start_in_path != start_in_path:
        changes_made = True

        # Update the shortcut with the new paths
        shortcut.path = new_target_path
        shortcut.working_directory = new_start_in_path
        shortcut.save()

        logging.info(f'Successfully updated {file_path}')
        print(f'Successfully updated {file_path}')
      else:
        logging.info(f'No changes made to {file_path}')
        print(f'No changes made to {file_path}')
    except Exception as e:
      logging.error(f'Failed to update {file_path}: {str(e)}')
      print(f'Failed to update {file_path}: {str(e)}')

  # Update the progress bar
  progress_bar.update(1)

# Close the progress bar
progress_bar.close()

# Log if no changes were made
if not changes_made:
  logging.info('No changes were made during this run.')
  print('No changes were made during this run.')