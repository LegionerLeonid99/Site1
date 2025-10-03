#!/usr/bin/env python3
"""
Main Flask application entry point.
Run this file to start the development server.
"""

import os
from app import create_app

# Create the Flask application
app = create_app(os.getenv('FLASK_ENV', 'default'))

if __name__ == '__main__':
    # Run the development server
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"Starting Flask server on port {port}")
    print(f"Debug mode: {debug}")
    print(f"Environment: {os.getenv('FLASK_ENV', 'development')}")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
