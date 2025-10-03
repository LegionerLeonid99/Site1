# PowerShell script to start the Flask backend
# Run this with: .\start.ps1

Write-Host "Starting FixIt Appliances Backend Server..." -ForegroundColor Green
Write-Host ""

# Change to backend directory
Set-Location "e:\Site1\Gau\backend"

# Check if .env file exists
if (-not (Test-Path ".env")) {
    Write-Host "Warning: .env file not found. Please copy .env.example to .env and configure your settings." -ForegroundColor Red
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

# Start the Flask development server
Write-Host "Flask server will be available at: http://localhost:5000" -ForegroundColor Cyan
Write-Host "API endpoints will be available at: http://localhost:5000/api/" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

python app.py
