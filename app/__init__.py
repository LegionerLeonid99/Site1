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

  # Configure CORS
  allow_null = os.getenv('ALLOW_NULL_ORIGIN', 'false').lower() == 'true'
  debug_mode = app.config.get('DEBUG', False)
  # In development allow all origins unless explicitly disabled
  if debug_mode and os.getenv('DISABLE_DEV_WILDCARD_CORS', 'false').lower() != 'true':
    CORS(app, resources={r"/api/*": {"origins": "*"}}, allow_headers=["Content-Type"], supports_credentials=False)
  else:
    origins = app.config.get('ALLOWED_ORIGINS', [])
    if allow_null:
      origins.append('null')
    CORS(app, resources={r"/api/*": {"origins": origins}}, allow_headers=["Content-Type"], supports_credentials=True)

  # Add request logging middleware
  @app.before_request
  def log_request_info():
    print(f"[REQUEST] {request.method} {request.path} from {request.remote_addr}", file=sys.stderr)
    print(f"[HEADERS] {dict(request.headers)}", file=sys.stderr)

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
    print(f"[SERVE] Requested path: {path}, static_folder: {app.static_folder}", file=sys.stderr)
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
      return send_from_directory(app.static_folder, path)
    else:
      return send_from_directory(app.static_folder, 'index.html')

  return app
