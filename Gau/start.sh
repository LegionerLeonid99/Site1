#!/bin/bash

# Build frontend
echo "Building frontend..."
npm install
npm run build

# Install Python dependencies
echo "Installing Python dependencies..."
cd backend
pip install -r requirements.txt
pip install gunicorn

# Start the application
echo "Starting application..."
gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 120 --access-logfile - --error-logfile - app:app
