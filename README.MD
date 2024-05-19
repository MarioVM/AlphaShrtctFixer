alphascf.py
This Python script is designed to change the drive letter of the target and working directory paths of all shortcut files (.lnk files) in the directory where the script is located to the letter W.

This is the reason why I started the other app ShrctFixer

How it works
It first gets the current directory where the script is running.
It then iterates over all the files in this directory.
For each file, it checks if the file is a shortcut (i.e., if it ends with .lnk).
If the file is a shortcut, it uses the winshell library to get a shortcut object.
It then retrieves the current target path and working directory of the shortcut.
It replaces the drive letter of these paths with "W".
Finally, it updates the shortcut with the new paths and saves the changes.

Requirements
This script requires the winshell library. You can install it using pip:

pip install winshell tqdm

Usage
To use this script, simply run it in the directory containing the .lnk files you want to modify:

python alphascf.py

Please note that this script will only work on Windows, as it uses the winshell library, which is a light wrapper around the Windows Shell functionality, and .lnk files are a Windows-specific file format for shortcuts.