@echo off
REM Development server startup script for FixIt Appliances Backend

echo Starting FixIt Appliances Backend Server...
echo.

REM Change to backend directory
cd /d "e:\Site1\Gau\backend"

REM Check if .env file exists
if not exist ".env" (
    echo Warning: .env file not found. Please copy .env.example to .env and configure your settings.
    echo.
    pause
    exit /b 1
)

REM Start the Flask development server
echo Flask server will be available at: http://localhost:5000
echo API endpoints will be available at: http://localhost:5000/api/
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py
