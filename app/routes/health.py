from flask import Blueprint, jsonify, current_app
import os

health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'O-TECH HOME SERVICES API is running',
        'version': '1.0.0'
    }), 200

@health_bp.route('/debug', methods=['GET'])
def debug_info():
    """Diagnostic endpoint to check static files and configuration"""
    static_folder = current_app.static_folder
    static_exists = os.path.exists(static_folder) if static_folder else False
    
    static_files = []
    if static_exists:
        try:
            static_files = os.listdir(static_folder)[:20]  # First 20 files
        except Exception as e:
            static_files = [f"Error listing: {str(e)}"]
    
    return jsonify({
        'status': 'debug',
        'cwd': os.getcwd(),
        'static_folder': static_folder,
        'static_exists': static_exists,
        'static_file_count': len(os.listdir(static_folder)) if static_exists else 0,
        'static_files_sample': static_files,
        'environment': os.getenv('FLASK_ENV', 'not set'),
        'port': os.getenv('PORT', 'not set')
    }), 200

