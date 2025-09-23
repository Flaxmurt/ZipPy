@echo off
setlocal enabledelayedexpansion

:: --- Configuration ---
:: This should match the name of your Python script.
set "SCRIPT_NAME=zippy.py"

:: Default values for the prompts.
set "DEFAULT_CHUNK_SIZE=10"
set "DEFAULT_MAX_MB=100"
:: ---------------------

:: Ensure a folder was dragged onto the script.
if "%~1"=="" (
    echo ERROR: You must drag and drop a folder onto this file to process it.
    echo.
    pause
    exit /b
)
set "SRC_DIR=%~1"
cls

:: --- User Interface ---
echo Zippy Archiver
echo ==================
echo.
echo Source Folder: "%SRC_DIR%"
echo.
echo Select archiving mode:
echo   1. Context Mode (Combine files by type, then zip)
echo   2. Direct Mode  (Zip all individual files directly)
echo.
set "MODE_CHOICE="
choice /c 12 /n /m "Enter your choice (1 or 2): "

if errorlevel 2 (
    set "ZIP_MODE=direct"
) else (
    set "ZIP_MODE=context"
)

echo.
echo --- Configuring !ZIP_MODE! mode ---

:: --- Gather Settings Based on Mode ---
if "!ZIP_MODE!"=="context" (
    set "MAX_SIZE_INPUT="
    set /p "MAX_SIZE_INPUT=Enter max context file size in MB (Default: %DEFAULT_MAX_MB%): "
    if "%MAX_SIZE_INPUT%"=="" (
        set "MAX_SIZE_MB=%DEFAULT_MAX_MB%"
    ) else (
        set "MAX_SIZE_MB=%MAX_SIZE_INPUT%"
    )
    
    set "CHUNK_SIZE_INPUT="
    set /p "CHUNK_SIZE_INPUT=Enter number of context files per zip (Default: %DEFAULT_CHUNK_SIZE%): "
    if "%CHUNK_SIZE_INPUT%"=="" (
        set "CHUNK_SIZE=%DEFAULT_CHUNK_SIZE%"
    ) else (
        set "CHUNK_SIZE=%CHUNK_SIZE_INPUT%"
    )

    :: Construct the final arguments for the python script using delayed expansion.
    set "FINAL_ARGS=--mode context --max-size !MAX_SIZE_MB! -s !CHUNK_SIZE!"

) else (
    set "CHUNK_SIZE_INPUT="
    set /p "CHUNK_SIZE_INPUT=Enter number of files per zip archive (Default: %DEFAULT_CHUNK_SIZE%): "
    if "%CHUNK_SIZE_INPUT%"=="" (
        set "CHUNK_SIZE=%DEFAULT_CHUNK_SIZE%"
    ) else (
        set "CHUNK_SIZE=%CHUNK_SIZE_INPUT%"
    )
    
    :: Construct the final arguments for the python script using delayed expansion.
    set "FINAL_ARGS=--mode direct -s !CHUNK_SIZE!"
)

echo.
echo --- Starting Python Script ---
echo.
:: Execute the Python script with the source folder and the chosen arguments.
python "%~dp0%SCRIPT_NAME%" "%SRC_DIR%" %FINAL_ARGS%

echo.
echo --- Script Finished ---
pause
endlocal