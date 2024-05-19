import os
import winshell
import logging
from tqdm import tqdm
from datetime import datetime

# Set up logging
logging.basicConfig(filename='alphascf.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Function to update shortcuts in the specified folder
def update_shortcuts(folder_path):
    # Get all the files in the specified folder
    files = os.listdir(folder_path)

    # Create a progress bar
    progress_bar = tqdm(total=len(files), position=0, leave=True)

    # Initialize a flag to check if any changes were made
    changes_made = False

    # Iterate over all the files in the specified folder
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        # Check if the file is a shortcut
        if file_path.lower().endswith('.lnk'):
            try:
                # Get the shortcut object
                shortcut = winshell.shortcut(file_path)

                # Get the current target and start in paths
                target_path = shortcut.path
                start_in_path = shortcut.working_directory

                # Check if the target and start in paths are valid
                if len(target_path) > 0 and len(start_in_path) > 0:
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

                        logging.info(f'Successfully updated {file_path}')
                        print(f'Successfully updated {file_path}')
                    else:
                        logging.info(f'No changes made to {file_path}')
                        print(f'No changes made to {file_path}')
                else:
                    logging.error(f'Invalid target or start in path for {file_path}')
                    print(f'Invalid target or start in path for {file_path}')
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

# Main function to get the folder path from the user
def main():
    folder_path = input("Enter the path of the folder containing the shortcuts: ")
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        update_shortcuts(folder_path)
    else:
        print("The specified path is not a valid directory.")

if __name__ == "__main__":
    main()
