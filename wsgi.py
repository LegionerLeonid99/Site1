#!/usr/bin/env python3
"""
Main Flask application entry point.
Run this file to start the development server.
"""

import os
import sys
from app import create_app

# Add diagnostic logging on startup
print("=" * 80, file=sys.stderr)
print("WSGI STARTUP DIAGNOSTICS", file=sys.stderr)
print("=" * 80, file=sys.stderr)
print(f"Working directory: {os.getcwd()}", file=sys.stderr)
print(f"Python path: {sys.path}", file=sys.stderr)
print(f"FLASK_ENV: {os.getenv('FLASK_ENV', 'default')}", file=sys.stderr)
print(f"PORT: {os.getenv('PORT', 'not set')}", file=sys.stderr)

# Check static folder
static_path = os.path.join(os.getcwd(), 'static')
print(f"\nStatic folder path: {static_path}", file=sys.stderr)
print(f"Static folder exists: {os.path.exists(static_path)}", file=sys.stderr)
if os.path.exists(static_path):
    files = os.listdir(static_path)
    print(f"Static folder contents ({len(files)} items):", file=sys.stderr)
    for f in files[:10]:  # Show first 10 files
        print(f"  - {f}", file=sys.stderr)
    if len(files) > 10:
        print(f"  ... and {len(files) - 10} more files", file=sys.stderr)
else:
    print("  WARNING: Static folder does not exist!", file=sys.stderr)

print("=" * 80, file=sys.stderr)

# Create the Flask application
app = create_app(os.getenv('FLASK_ENV', 'default'))

print(f"Flask app created successfully", file=sys.stderr)
print(f"Static folder configured as: {app.static_folder}", file=sys.stderr)
print(f"Registered routes:", file=sys.stderr)
for rule in app.url_map.iter_rules():
    print(f"  {rule.rule} -> {rule.endpoint}", file=sys.stderr)
print("=" * 80, file=sys.stderr)

if __name__ == '__main__':
    # Run the development server
    port = int(os.getenv('PORT', 8000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"Starting Flask server on port {port}")
    print(f"Debug mode: {debug}")
    print(f"Environment: {os.getenv('FLASK_ENV', 'development')}")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
