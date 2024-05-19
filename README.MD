alphascf.py
This Python script is designed to change the drive letter of the target and working directory paths of all shortcut files (.lnk files) in the directory where the script is located to the letter W.

This is the reason why I started the other app ShrctFixer

# Shortcut Drive Letter Updater

This script iterates over all the shortcut files (.lnk) in a specified folder and updates their target and start-in paths to use the drive letter "W". If the new paths with "W" do not exist, the drive letter is changed to "F".

## Prerequisites

- Python 3.x
- `winshell` library
- `tqdm` library

## Installation

1. **Install Python**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

2. **Install required libraries**:
    ```bash
    pip install winshell tqdm
    ```

## Usage

1. **Clone the repository or download the script**.

2. **Run the script**:

    - Open Command Prompt as Administrator (necessary for modifying shortcut files):
        - Press the `Windows` key, type `cmd`, right-click on `Command Prompt`, and select `Run as administrator`.

    - Navigate to the directory containing the script:
        ```bash
        cd path\to\your\script
        ```

    - Run the script:
        ```bash
        python your_script.py
        ```

3. **Enter the folder path** when prompted. The script will process all shortcut files in the specified folder.

## Example

```bash
Enter the path of the folder containing the shortcuts: C:\Gaming

Logging: The script logs its actions to a file named alphascf.log.
Progress Bar: A progress bar is displayed to show the script's progress.
Permission Handling: The script checks and handles permissions to ensure it can modify the shortcut files.
Error Handling
The script logs and prints errors if it encounters issues such as "Access is denied" or invalid file paths.
If a shortcut's target or start-in path cannot be changed to "W", the script will attempt to change the drive letter to "F".
Contributing
Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.

License
This project is licensed under the GNU GENERAL PUBLIC LICENSE.