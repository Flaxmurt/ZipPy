@echo off
setlocal

:: --- CONFIGURATION ---
:: 1. SET THE EXACT NAME OF YOUR PYTHON SCRIPT.
set "SCRIPT_NAME=zippy.py"

:: 2. Set the default number of files you want in each archive.
set "DEFAULT_SIZE=10"

:: 3. Set a name for the subfolder where archives will be saved.
set "DEFAULT_OUTPUT_SUBFOLDER=_archives"
:: ---------------------

:: Check if a folder path was provided (e.g., via drag-and-drop)
if "%~1"=="" (
    echo ERROR: Missing input. You must drag and drop a folder onto this file.
    echo.
    pause
    exit /b
)
set "SRC_DIR=%~1"

:: Prompt for the number of files per archive
echo Source Folder: "%SRC_DIR%"
echo.
set "CHUNK_SIZE="
set /p "CHUNK_SIZE=Enter files per archive (Press Enter for default: %DEFAULT_SIZE%): "
if not defined CHUNK_SIZE (
    set "CHUNK_SIZE=%DEFAULT_SIZE%"
)

:: Set the final output directory
:: <<< MODIFIED: This now saves archives to a folder next to the script.
set "OUTPUT_DIR=%~dp0%DEFAULT_OUTPUT_SUBFOLDER%_%~n1"

echo.
echo --- Starting Python Script ---
echo.

:: Execute the Python script with the correct arguments
python "%~dp0%SCRIPT_NAME%" "%SRC_DIR%" -s %CHUNK_SIZE% -o "%OUTPUT_DIR%"

echo.
echo --- Script Finished ---
pause
endlocal