@echo off
chcp 65001 >nul
cls
color 0A

echo  Pynux Terminal 1.0.x
echo  Created by MrAnergos
echo.

timeout /t 1 >nul
echo Installing Python libraries...
timeout /t 1 >nul

python -m pip install --quiet colorama pystyle rich prompt_toolkit requests pygments psutil wmi pyttsx3

if %ERRORLEVEL% NEQ 0 (
    color 0C
    echo [!] ERROR: Failed to install Python libraries.
    pause
    exit /b
)

color 0A
echo.
echo [✓] All Python libraries installed successfully!
echo.
echo Do you want to run main.py as administrator? (Y/N)
set /p adminchoice=Your choice: 

if /I "%adminchoice%"=="Y" (
    REM Run as administrator
    powershell -Command "Start-Process python -ArgumentList 'main.py' -Verb RunAs"
) else (
    REM Run normally
    python main.py
)
pause
