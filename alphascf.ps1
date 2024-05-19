# Get the directory of the current script
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Set the path to the Python script
$pythonScript = Join-Path -Path $scriptDir -ChildPath "alphascf.py"

# Check if the Python script exists
if (Test-Path $pythonScript) {
    # Run the Python script
    python $pythonScript
} else {
    Write-Host "The file 'alphascf.py' was not found in the script directory."
}

# Keep the console window open until the user presses Enter
Write-Host "Press Enter to close the window..."
Read-Host
