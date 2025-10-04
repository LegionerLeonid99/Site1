from flask import Flask, send_from_directory, request
from flask_cors import CORS
from flask_mail import Mail
from config.config import config
import os
import sys

mail = Mail()

def create_app(config_name='default'):
  app = Flask(__name__, static_folder=os.path.join(os.getcwd(), 'static'), static_url_path='')
  app.config.from_object(config[config_name])

  # Initialize extensions
  mail.init_app(app)

  # Configure CORS - allow all origins in production for Railway to work
  CORS(app, resources={
    r"/api/*": {
      "origins": "*",
      "methods": ["GET", "POST", "OPTIONS"],
      "allow_headers": ["Content-Type"],
      "supports_credentials": False
    }
  })

  # Add request logging middleware with error handling
  @app.before_request
  def log_request_info():
    try:
      print(f"[REQUEST] {request.method} {request.path} from {request.remote_addr}", file=sys.stderr, flush=True)
    except Exception as e:
      print(f"[REQUEST LOG ERROR] {e}", file=sys.stderr, flush=True)

  # Register blueprints
  from app.routes.contact import contact_bp
  from app.routes.newsletter import newsletter_bp
  from app.routes.health import health_bp

  app.register_blueprint(contact_bp, url_prefix='/api')
  app.register_blueprint(newsletter_bp, url_prefix='/api')
  app.register_blueprint(health_bp, url_prefix='/api')

  # Serve frontend static files in production
  @app.route('/', defaults={'path': ''})
  @app.route('/<path:path>')
  def serve_frontend(path):
    """Serve frontend files or index.html for client-side routing"""
    try:
      print(f"[SERVE] Requested path: '{path}'", file=sys.stderr, flush=True)
      if path and path != "":
        file_path = os.path.join(app.static_folder, path)
        if os.path.exists(file_path) and os.path.isfile(file_path):
          print(f"[SERVE] Serving file: {file_path}", file=sys.stderr, flush=True)
          return send_from_directory(app.static_folder, path)
      # Default to index.html for SPA routing
      print(f"[SERVE] Serving index.html", file=sys.stderr, flush=True)
      return send_from_directory(app.static_folder, 'index.html')
    except Exception as e:
      print(f"[SERVE ERROR] {e}", file=sys.stderr, flush=True)
      return str(e), 500

  return app
