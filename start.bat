@echo off
setlocal
cd /d "%~dp0"

echo ==========================================
echo        EDA and Visualization - Start
echo ==========================================
echo.

if not exist "venv\Scripts\python.exe" (
    echo ERROR: Project environment is not set up.
    echo Please run setup.bat first.
    pause
    exit /b 1
)

if not exist "eda.py" (
    echo ERROR: eda.py was not found in:
    echo %CD%
    pause
    exit /b 1
)

if not exist "data\sample_dataset.csv" (
    echo ERROR: Dataset not found: data\sample_dataset.csv
    echo Please check the data folder and DATA_FILE in eda.py.
    pause
    exit /b 1
)

echo Running EDA analysis...
echo.
"venv\Scripts\python.exe" "eda.py"
set "RUN_EXIT=%errorlevel%"

echo.
if not "%RUN_EXIT%"=="0" (
    echo Project finished with an error. Review the message above.
) else (
    echo Project completed successfully.
    echo Generated files are available in the outputs folder.
)
echo.
pause
exit /b %RUN_EXIT%
