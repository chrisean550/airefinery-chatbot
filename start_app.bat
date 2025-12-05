@echo off
REM Start AI Refinery app: create venv, install deps, activate and run main.py

SETLOCAL

IF NOT EXIST ".venv\Scripts\activate.bat" (
  echo Creating virtual environment...
  python -m venv .venv
  if errorlevel 1 (
    echo Failed to create virtualenv. Ensure Python is on PATH.
    exit /b 1
  )
  echo Upgrading pip and installing dependencies...
  .venv\Scripts\python.exe -m pip install --upgrade pip
  if errorlevel 1 (
    echo Failed to upgrade pip.
    exit /b 1
  )
  .venv\Scripts\python.exe -m pip install -r requirements.txt
  if errorlevel 1 (
    echo Failed to install dependencies.
    exit /b 1
  )
) else (
  echo Virtual environment found.
)

IF NOT EXIST ".env" (
  IF EXIST ".env.example" (
    copy /Y ".env.example" ".env" >nul
    echo Created .env from .env.example. Please edit .env to set AIR_API_KEY if needed.
  ) else (
    echo .env not found and .env.example missing. Please create a .env with AIR_API_KEY.
  )
)

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Running chat app...
python main.py

ENDLOCAL

pause
@echo off
REM Start AI Refinery app: create venv, install deps, activate and run main.py

SETLOCAL

































pause
nENDLOCALpython main.py
necho Running chat app...call .venv\Scripts\activate.batecho Activating virtual environment...)  )    echo Created .env from .env.example. Please edit .env to set AIR_API_KEY if needed.    copy /Y ".env.example" ".env" >nul  IF EXIST ".env.example" (IF NOT EXIST ".env" ()  echo Virtual environment found.) else (  )    exit /b 1    echo Failed to install dependencies.  if errorlevel 1 (  .venv\Scripts\python.exe -m pip install -r requirements.txt  .venv\Scripts\python.exe -m pip install --upgrade pip  echo Upgrading pip and installing dependencies...  )    exit /b 1    echo Failed to create virtualenv. Ensure Python is on PATH.  if errorlevel 1 (  python -m venv .venv  echo Creating virtual environment...nIF NOT EXIST ".venv\Scripts\activate.bat" (