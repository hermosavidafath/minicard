@echo off
echo Starting Rentry Application...
echo.

REM Check if virtual environment exists
if exist "env\Scripts\activate.bat" (
    echo Activating virtual environment...
    call env\Scripts\activate.bat
)

REM Check database
echo Checking database...
python db_manager.py check
echo.

REM Start application
echo Starting server...
python run.py

pause