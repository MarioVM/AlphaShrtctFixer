# Shortcut Drive Letter Updater

This project contains a Python script (`alphascf.py`) and a PowerShell script (`run_alphascf.ps1`) to update the drive letters in Windows shortcut files (.lnk) within a specified directory. The script changes the drive letters to "W" if the target and start-in paths are valid; otherwise, it changes them to "F".

## Prerequisites

- **Python 3.x**
- **Required Python libraries**:
  - `winshell`
  - `tqdm`
- **PowerShell**

## Installation

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/).

2. **Install required Python libraries**:
    ```bash
    pip install winshell tqdm
    ```

3. **Clone the repository or download the scripts**: Ensure both `alphascf.py` and `run_alphascf.ps1` are in the same directory.

## Usage

### Running the Python Script Directly

1. **Open Command Prompt as Administrator**:
    - Press the `Windows` key, type `cmd`, right-click on `Command Prompt`, and select `Run as administrator`.

2. **Navigate to the directory containing the scripts**:
    ```bash
    cd path\to\your\script\directory
    ```

3. **Run the Python script**:
    ```bash
    python alphascf.py
    ```

### Running the PowerShell Script

The PowerShell script requests elevated permissions and runs the Python script.

1. **Open PowerShell**.

2. **Navigate to the directory containing the scripts**:
    ```powershell
    cd path\to\your\script\directory
    ```

3. **Run the PowerShell script**:
    ```powershell
    .\run_alphascf.ps1
    ```

4. **Follow the prompt**: Enter the path of the folder containing the shortcuts when prompted. The script will process all shortcut files in the specified folder.

## Logging and Output

- The Python script logs its actions to a file named `alphascf.log`.
- A progress bar is displayed to show the script's progress.
- Errors and status messages are printed to the console.

## Example

```bash
Enter the path of the folder containing the shortcuts: C:\Gaming
Error Handling
The script logs and prints errors if it encounters issues such as "Access is denied" or invalid file paths.
If a shortcut's target or start-in path cannot be changed to "W", the script will attempt to change the drive letter to "F".
Contributing
Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.

License
This project is licensed under the GNU GENERAL PUBLIC LICENSE


### Notes
- **Ensure you have appropriate permissions**: The scripts need to run with elevated permissions to modify shortcut files in protected directories.
- **Check paths**: Make sure the paths you enter are valid and accessible.

By following these instructions, users can easily understand and use the scripts to update their shortcut files.
