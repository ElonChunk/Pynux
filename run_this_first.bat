@echo off
chcp 65001 >nul
cls
color 0A

REM Print your new banner
echo  Pynux 1.0.1v
echo  A Python-based terminal environment
echo  Created by MrAnergos ( Elon Chunk )
echo.

timeout /t 1 >nul
echo Installing Python libraries...
timeout /t 1 >nul

python -m pip install --quiet colorama pystyle rich prompt_toolkit requests

if %ERRORLEVEL% NEQ 0 (
    color 0C
    echo [!] ERROR: Failed to install Python libraries.
    pause
    exit /b
)

color 0A
echo.
echo [✓] All Python libraries installed successfully!
pause
