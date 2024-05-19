# Function to check and request elevated permissions
function Request-Elevation {
    $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
    $currentPrincipal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    $adminRole = [Security.Principal.WindowsBuiltInRole]::Administrator

    if (-not $currentPrincipal.IsInRole($adminRole)) {
        Write-Host "Requesting elevated permissions..."
        Start-Process powershell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
        exit
    }
}

# Request elevated permissions if not already running as administrator
Request-Elevation

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

# Keep the console window open 
