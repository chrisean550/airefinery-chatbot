# Create a venv and install requirements for airefinery-app
param(
    [string]$VenvName = ".venv"
)

python -m venv $VenvName
Write-Host "Virtualenv created at $VenvName"

# Install dependencies into the venv
& "$PWD\$VenvName\Scripts\python.exe" -m pip install --upgrade pip
& "$PWD\$VenvName\Scripts\python.exe" -m pip install -r requirements.txt
Write-Host "Dependencies installed. Activate the venv with:`n`& .\$VenvName\Scripts\Activate.ps1`nThen run: python main.py"