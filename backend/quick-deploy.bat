@echo off
echo 🚀 Rentry Quick Deploy
echo ======================

REM Check if git is initialized
if not exist ".git" (
    echo Initializing git repository...
    git init
    git add .
    git commit -m "Initial commit"
)

echo Choose deployment platform:
echo 1. Heroku
echo 2. Railway
echo 3. Render
echo 4. Docker
echo 5. Manual setup info

set /p choice="Enter choice (1-5): "

if "%choice%"=="1" (
    echo 🔧 Setting up Heroku deployment...
    where heroku >nul 2>nul
    if errorlevel 1 (
        echo ❌ Heroku CLI not installed. Install from: https://devcenter.heroku.com/articles/heroku-cli
        pause
        exit /b 1
    )
    
    set /p app_name="Enter app name: "
    heroku create %app_name%
    python -c "import secrets; print('heroku config:set SECRET_KEY=' + secrets.token_hex(32))" > temp_cmd.bat
    call temp_cmd.bat
    del temp_cmd.bat
    heroku config:set FLASK_ENV=production
    
    echo ✅ Heroku app created. Deploy with:
    echo git push heroku main
) else if "%choice%"=="2" (
    echo 🔧 Setting up Railway deployment...
    where railway >nul 2>nul
    if errorlevel 1 (
        echo Installing Railway CLI...
        npm install -g @railway/cli
    )
    
    echo ✅ Railway setup. Deploy with:
    echo railway login
    echo railway up
) else if "%choice%"=="3" (
    echo 🔧 Render deployment info:
    echo 1. Push code to GitHub
    echo 2. Connect repository to Render
    echo 3. Set build command: pip install -r requirements.txt
    echo 4. Set start command: gunicorn wsgi:application
    echo 5. Add environment variables
) else if "%choice%"=="4" (
    echo 🔧 Building Docker image...
    docker build -t rentry-app .
    echo ✅ Docker image built. Run with:
    echo docker run -p 5000:5000 -e SECRET_KEY=your-secret-key rentry-app
) else if "%choice%"=="5" (
    echo 📋 Manual deployment checklist:
    echo 1. Set environment variables:
    echo    SECRET_KEY=your-secret-key
    echo    FLASK_ENV=production
    echo    DATABASE_URL=your-database-url
    echo.
    echo 2. Install dependencies:
    echo    pip install -r requirements.txt
    echo.
    echo 3. Initialize database:
    echo    python db_manager.py init
    echo.
    echo 4. Run with gunicorn:
    echo    gunicorn wsgi:application
) else (
    echo ❌ Invalid choice
    pause
    exit /b 1
)

echo.
echo 🎉 Setup complete! Check DEPLOYMENT.md for detailed instructions.
pause