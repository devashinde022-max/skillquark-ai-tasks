@echo off
echo Installing required packages...
python -m pip install -r requirements.txt
echo.
echo Running EDA project...
python eda.py
echo.
pause
